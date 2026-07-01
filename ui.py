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
from i18n import translate
from keyboard_simulator import (
    TypingCancelled,
    configure_safety,
    countdown,
    type_text,
)


class TypingApp:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.language = "pt"
        self.root.title(self._t("app_title"))
        self.root.geometry("760x620")
        self.root.minsize(620, 520)

        self.cancel_event = threading.Event()
        self.worker: threading.Thread | None = None

        self.initial_delay_var = tk.StringVar(value=str(DEFAULT_INITIAL_DELAY_SECONDS))
        self.interval_var = tk.StringVar(value=str(DEFAULT_CHARACTER_INTERVAL_SECONDS))
        self.status_var = tk.StringVar(value=self._t("ready"))

        configure_safety()
        self._build_ui()
        self.root.bind("<Escape>", self._on_escape)
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    def run(self) -> None:
        self.root.mainloop()

    def _t(self, key: str) -> str:
        return translate(self.language, key)

    def _build_ui(self) -> None:
        main_frame = ttk.Frame(self.root, padding=16)
        main_frame.pack(fill=tk.BOTH, expand=True)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        main_frame.rowconfigure(5, weight=1)

        self.title_label = ttk.Label(
            main_frame,
            text=self._t("app_title"),
            font=("Segoe UI", 16, "bold"),
        )
        self.title_label.grid(row=0, column=0, sticky="w")

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

        self.initial_delay_label = ttk.Label(settings_frame, text=self._t("initial_delay"))
        self.initial_delay_label.grid(
            row=0, column=0, sticky="w", padx=(0, 8)
        )
        ttk.Entry(settings_frame, textvariable=self.initial_delay_var, width=12).grid(
            row=0, column=1, sticky="w", padx=(0, 24)
        )

        self.interval_label = ttk.Label(settings_frame, text=self._t("character_interval"))
        self.interval_label.grid(
            row=0, column=2, sticky="w", padx=(0, 8)
        )
        ttk.Entry(settings_frame, textvariable=self.interval_var, width=12).grid(
            row=0, column=3, sticky="w"
        )

        self.instruction_label = ttk.Label(
            main_frame,
            text=self._t("instruction"),
            foreground="#444444",
        )
        self.instruction_label.grid(row=3, column=0, sticky="w", pady=(14, 10))

        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=0, sticky="ew")

        self.start_button = ttk.Button(
            button_frame,
            text=self._t("start"),
            command=self._start_typing,
        )
        self.start_button.pack(side=tk.LEFT)

        self.quick_test_button = ttk.Button(
            button_frame,
            text=self._t("quick_test"),
            command=self._start_quick_test,
        )
        self.quick_test_button.pack(side=tk.LEFT, padx=(8, 0))

        self.cancel_button = ttk.Button(
            button_frame,
            text=self._t("cancel"),
            command=self._cancel_typing,
            state=tk.DISABLED,
        )
        self.cancel_button.pack(side=tk.LEFT, padx=(8, 0))

        self.language_button = ttk.Button(
            button_frame,
            text=self._t("language"),
            command=self._toggle_language,
        )
        self.language_button.pack(side=tk.LEFT, padx=(8, 0))

        self.log_frame = ttk.LabelFrame(main_frame, text=self._t("status"))
        self.log_frame.grid(row=5, column=0, sticky="nsew", pady=(14, 0))
        self.log_frame.columnconfigure(0, weight=1)
        self.log_frame.rowconfigure(0, weight=1)

        self.log_output = scrolledtext.ScrolledText(
            self.log_frame,
            height=8,
            wrap=tk.WORD,
            state=tk.DISABLED,
        )
        self.log_output.grid(row=0, column=0, sticky="nsew", padx=8, pady=8)

        status_label = ttk.Label(main_frame, textvariable=self.status_var)
        status_label.grid(row=6, column=0, sticky="w", pady=(8, 0))

        self._log(self._t("ready_log"))

    def _start_typing(self) -> None:
        if self.worker is not None and self.worker.is_alive():
            return

        text = self.text_input.get("1.0", tk.END).rstrip("\n")
        if not text:
            messagebox.showwarning(self._t("empty_title"), self._t("empty_message"))
            return

        try:
            initial_delay = self._parse_float(
                self.initial_delay_var.get(),
                self._t("initial_delay_name"),
                MIN_INITIAL_DELAY_SECONDS,
            )
            interval = self._parse_float(
                self.interval_var.get(),
                self._t("character_interval_name"),
                MIN_CHARACTER_INTERVAL_SECONDS,
                MAX_CHARACTER_INTERVAL_SECONDS,
            )
        except ValueError as exc:
            messagebox.showwarning(self._t("invalid_title"), str(exc))
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
        message = self._t("quick_confirm_message") if quick_test else self._t("confirm_message")
        confirmed = messagebox.askyesno(self._t("confirm_title"), message)
        if not confirmed:
            self._log(self._t("cancelled_before_start"))
            return

        self.cancel_event.clear()
        self._set_running(True)
        if quick_test:
            self._log(self._t("quick_started"))
        else:
            self._log(self._t("countdown_started"))

        self.worker = threading.Thread(
            target=self._typing_worker,
            args=(text, initial_delay, interval),
            daemon=True,
        )
        self.worker.start()

    def _typing_worker(self, text: str, initial_delay: float, interval: float) -> None:
        try:
            self._thread_log(self._t("click_target"))
            countdown(initial_delay, self.cancel_event, self._thread_log)
            self._thread_log(self._t("typing_started"))
            type_text(text, interval, self.cancel_event, self._thread_log)
            self._thread_log(self._t("typing_done"))
        except TypingCancelled as exc:
            self._thread_log(str(exc))
        except Exception as exc:
            self._thread_log(f"{self._t('unexpected_error')} {exc}")
        finally:
            self.root.after(0, lambda: self._set_running(False))

    def _cancel_typing(self) -> None:
        self.cancel_event.set()
        self._log(self._t("cancel_requested"))

    def _on_escape(self, _event: tk.Event) -> str:
        self._cancel_typing()
        return "break"

    def _on_close(self) -> None:
        if self.worker is not None and self.worker.is_alive():
            self.cancel_event.set()
        self.root.destroy()

    def _toggle_language(self) -> None:
        if self.worker is not None and self.worker.is_alive():
            return

        self.language = "en" if self.language == "pt" else "pt"
        self._refresh_language()
        self._log(self._t("ready_log"))

    def _refresh_language(self) -> None:
        self.root.title(self._t("app_title"))
        self.title_label.configure(text=self._t("app_title"))
        self.instruction_label.configure(text=self._t("instruction"))
        self.initial_delay_label.configure(text=self._t("initial_delay"))
        self.interval_label.configure(text=self._t("character_interval"))
        self.start_button.configure(text=self._t("start"))
        self.quick_test_button.configure(text=self._t("quick_test"))
        self.cancel_button.configure(text=self._t("cancel"))
        self.language_button.configure(text=self._t("language"))
        self.log_frame.configure(text=self._t("status"))
        self.status_var.set(self._t("ready"))

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
            raise ValueError(self._t("field_number").format(field_name=field_name)) from exc

        if value < minimum:
            raise ValueError(
                self._t("minimum").format(field_name=field_name, minimum=minimum)
            )

        if maximum is not None and value > maximum:
            raise ValueError(
                self._t("maximum").format(field_name=field_name, maximum=maximum)
            )

        return value

    def _set_running(self, is_running: bool) -> None:
        self.start_button.configure(state=tk.DISABLED if is_running else tk.NORMAL)
        self.quick_test_button.configure(state=tk.DISABLED if is_running else tk.NORMAL)
        self.cancel_button.configure(state=tk.NORMAL if is_running else tk.DISABLED)
        self.language_button.configure(state=tk.DISABLED if is_running else tk.NORMAL)
        self.status_var.set(self._t("running") if is_running else self._t("ready"))

    def _thread_log(self, message: str) -> None:
        self.root.after(0, lambda: self._log(message))

    def _log(self, message: str) -> None:
        self.status_var.set(message)
        self.log_output.configure(state=tk.NORMAL)
        self.log_output.insert(tk.END, f"{message}\n")
        self.log_output.see(tk.END)
        self.log_output.configure(state=tk.DISABLED)
