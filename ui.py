from __future__ import annotations

import threading
import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk

from config import (
    DEFAULT_CHARACTER_INTERVAL_SECONDS,
    DEFAULT_INITIAL_DELAY_SECONDS,
    MAX_CHARACTER_INTERVAL_SECONDS,
    MIN_CHARACTER_INTERVAL_SECONDS,
    MIN_INITIAL_DELAY_SECONDS,
)
from keyboard_simulator import (
    TypingCancelled,
    configure_safety,
    countdown,
    type_text,
)


class TypingApp:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("MLI-Knot-keyboard")
        self.root.geometry("760x620")
        self.root.minsize(620, 520)

        self.cancel_event = threading.Event()
        self.worker: threading.Thread | None = None

        self.initial_delay_var = tk.StringVar(value=str(DEFAULT_INITIAL_DELAY_SECONDS))
        self.interval_var = tk.StringVar(value=str(DEFAULT_CHARACTER_INTERVAL_SECONDS))
        self.status_var = tk.StringVar(value="Pronto.")

        configure_safety()
        self._build_ui()
        self.root.bind("<Escape>", self._on_escape)
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    def run(self) -> None:
        self.root.mainloop()

    def _build_ui(self) -> None:
        main_frame = ttk.Frame(self.root, padding=16)
        main_frame.pack(fill=tk.BOTH, expand=True)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        main_frame.rowconfigure(5, weight=1)

        title = ttk.Label(
            main_frame,
            text="MLI-Knot-keyboard",
            font=("Segoe UI", 16, "bold"),
        )
        title.grid(row=0, column=0, sticky="w")

        self.text_input = scrolledtext.ScrolledText(
            main_frame,
            height=12,
            wrap=tk.WORD,
            undo=True,
        )
        self.text_input.grid(row=1, column=0, sticky="nsew", pady=(12, 12))

        settings_frame = ttk.Frame(main_frame)
        settings_frame.grid(row=2, column=0, sticky="ew")
        settings_frame.columnconfigure(1, weight=1)
        settings_frame.columnconfigure(3, weight=1)

        ttk.Label(settings_frame, text="Atraso inicial (segundos):").grid(
            row=0, column=0, sticky="w", padx=(0, 8)
        )
        ttk.Entry(settings_frame, textvariable=self.initial_delay_var, width=12).grid(
            row=0, column=1, sticky="w", padx=(0, 24)
        )

        ttk.Label(settings_frame, text="Intervalo entre caracteres:").grid(
            row=0, column=2, sticky="w", padx=(0, 8)
        )
        ttk.Entry(settings_frame, textvariable=self.interval_var, width=12).grid(
            row=0, column=3, sticky="w"
        )

        instruction = ttk.Label(
            main_frame,
            text=(
                "Após clicar em iniciar, selecione o campo de destino antes da "
                "contagem terminar."
            ),
            foreground="#444444",
        )
        instruction.grid(row=3, column=0, sticky="w", pady=(14, 10))

        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=0, sticky="ew")

        self.start_button = ttk.Button(
            button_frame,
            text="Iniciar digitação",
            command=self._start_typing,
        )
        self.start_button.pack(side=tk.LEFT)

        self.quick_test_button = ttk.Button(
            button_frame,
            text="Teste rápido",
            command=self._start_quick_test,
        )
        self.quick_test_button.pack(side=tk.LEFT, padx=(8, 0))

        self.cancel_button = ttk.Button(
            button_frame,
            text="Cancelar",
            command=self._cancel_typing,
            state=tk.DISABLED,
        )
        self.cancel_button.pack(side=tk.LEFT, padx=(8, 0))

        log_frame = ttk.LabelFrame(main_frame, text="Status")
        log_frame.grid(row=5, column=0, sticky="nsew", pady=(14, 0))
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)

        self.log_output = scrolledtext.ScrolledText(
            log_frame,
            height=8,
            wrap=tk.WORD,
            state=tk.DISABLED,
        )
        self.log_output.grid(row=0, column=0, sticky="nsew", padx=8, pady=8)

        status_label = ttk.Label(main_frame, textvariable=self.status_var)
        status_label.grid(row=6, column=0, sticky="w", pady=(8, 0))

        self._log("Pronto. Cole ou digite o texto com acentos na caixa acima.")

    def _start_typing(self) -> None:
        if self.worker is not None and self.worker.is_alive():
            return

        text = self.text_input.get("1.0", tk.END).rstrip("\n")
        if not text:
            messagebox.showwarning("Texto vazio", "Informe o texto a ser digitado.")
            return

        try:
            initial_delay = self._parse_float(
                self.initial_delay_var.get(),
                "atraso inicial",
                MIN_INITIAL_DELAY_SECONDS,
            )
            interval = self._parse_float(
                self.interval_var.get(),
                "intervalo entre caracteres",
                MIN_CHARACTER_INTERVAL_SECONDS,
                MAX_CHARACTER_INTERVAL_SECONDS,
            )
        except ValueError as exc:
            messagebox.showwarning("Valor inválido", str(exc))
            return

        self._begin_typing(text, initial_delay, interval)

    def _start_quick_test(self) -> None:
        if self.worker is not None and self.worker.is_alive():
            return

        self._begin_typing("abc123", 5.0, 0.1, quick_test=True)

    def _begin_typing(
        self,
        text: str,
        initial_delay: float,
        interval: float,
        quick_test: bool = False,
    ) -> None:
        message = (
            "Teste rápido: após confirmar, clique no Bloco de Notas durante a "
            "contagem regressiva.\n\nDeseja iniciar?"
            if quick_test
            else "Após confirmar, clique no campo de destino durante a contagem regressiva.\n\n"
            "Deseja iniciar?"
        )
        confirmed = messagebox.askyesno("Confirmar digitação", message)
        if not confirmed:
            self._log("Operação cancelada antes do início.")
            return

        self.cancel_event.clear()
        self._set_running(True)
        if quick_test:
            self._log("Teste rápido iniciado. Digitará abc123 após 5 segundos.")
        else:
            self._log("Contagem regressiva iniciada.")

        self.worker = threading.Thread(
            target=self._typing_worker,
            args=(text, initial_delay, interval),
            daemon=True,
        )
        self.worker.start()

    def _typing_worker(self, text: str, initial_delay: float, interval: float) -> None:
        try:
            self._thread_log("Clique no campo de destino agora.")
            countdown(initial_delay, self.cancel_event, self._thread_log)
            self._thread_log("Digitação iniciada.")
            type_text(text, interval, self.cancel_event, self._thread_log)
            self._thread_log("Digitação concluída com sucesso.")
        except TypingCancelled as exc:
            self._thread_log(str(exc))
        except Exception as exc:
            self._thread_log(f"Erro inesperado: {exc}")
        finally:
            self.root.after(0, lambda: self._set_running(False))

    def _cancel_typing(self) -> None:
        self.cancel_event.set()
        self._log("Cancelamento solicitado.")

    def _on_escape(self, _event: tk.Event) -> str:
        self._cancel_typing()
        return "break"

    def _on_close(self) -> None:
        if self.worker is not None and self.worker.is_alive():
            self.cancel_event.set()
        self.root.destroy()

    def _parse_float(
        self,
        raw_value: str,
        field_name: str,
        minimum: float,
        maximum: float | None = None,
    ) -> float:
        try:
            value = float(raw_value.strip().replace(",", "."))
        except ValueError as exc:
            raise ValueError(f"Informe um número válido para {field_name}.") from exc

        if value < minimum:
            raise ValueError(f"O valor mínimo para {field_name} é {minimum}.")

        if maximum is not None and value > maximum:
            raise ValueError(f"O valor máximo para {field_name} é {maximum}.")

        return value

    def _set_running(self, is_running: bool) -> None:
        self.start_button.configure(state=tk.DISABLED if is_running else tk.NORMAL)
        self.quick_test_button.configure(state=tk.DISABLED if is_running else tk.NORMAL)
        self.cancel_button.configure(state=tk.NORMAL if is_running else tk.DISABLED)
        self.status_var.set("Executando..." if is_running else "Pronto.")

    def _thread_log(self, message: str) -> None:
        self.root.after(0, lambda: self._log(message))

    def _log(self, message: str) -> None:
        self.status_var.set(message)
        self.log_output.configure(state=tk.NORMAL)
        self.log_output.insert(tk.END, f"{message}\n")
        self.log_output.see(tk.END)
        self.log_output.configure(state=tk.DISABLED)
