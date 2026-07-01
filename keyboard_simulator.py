from __future__ import annotations

import ctypes
import sys
import time
import traceback
from collections.abc import Callable
from ctypes import wintypes
from threading import Event

import pyautogui

from config import COUNTDOWN_STEP_SECONDS


user32 = ctypes.WinDLL("user32", use_last_error=True) if sys.platform == "win32" else None

INPUT_MOUSE = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_KEYUP = 0x0002
KEYEVENTF_UNICODE = 0x0004
ULONG_PTR = wintypes.WPARAM


class TypingCancelled(Exception):
    """Raised when typing is cancelled safely by the user."""


def configure_safety() -> None:
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0


def _sleep_with_cancel(seconds: float, cancel_event: Event) -> None:
    deadline = time.monotonic() + seconds
    while time.monotonic() < deadline:
        ensure_not_cancelled(cancel_event)
        time.sleep(min(0.05, deadline - time.monotonic()))


def ensure_not_cancelled(cancel_event: Event) -> None:
    if cancel_event.is_set():
        raise TypingCancelled("Digitacao cancelada pelo usuario.")

    if pyautogui.FAILSAFE:
        try:
            mouse_position = tuple(pyautogui.position())
        except pyautogui.FailSafeException as exc:
            raise TypingCancelled(
                "Digitacao cancelada pelo mecanismo de seguranca do mouse."
            ) from exc

        fail_safe_points = getattr(pyautogui, "FAILSAFE_POINTS", [(0, 0)])
        if mouse_position in fail_safe_points:
            raise TypingCancelled(
                "Digitacao cancelada pelo mecanismo de seguranca do mouse."
            )


def countdown(
    seconds: float,
    cancel_event: Event,
    status_callback: Callable[[str], None] | None = None,
) -> None:
    remaining = int(seconds)
    while remaining > 0:
        ensure_not_cancelled(cancel_event)
        _notify(
            status_callback,
            f"Iniciando em {remaining} segundo(s). Clique no campo de destino agora.",
        )
        _sleep_with_cancel(COUNTDOWN_STEP_SECONDS, cancel_event)
        remaining -= 1

    fractional_part = seconds - int(seconds)
    if fractional_part > 0:
        _sleep_with_cancel(fractional_part, cancel_event)


def type_text(
    text: str,
    interval_seconds: float,
    cancel_event: Event,
    status_callback: Callable[[str], None] | None = None,
) -> None:
    try:
        _notify(
            status_callback,
            "Digitação iniciada. Verifique se o campo de destino está focado.",
        )
        if sys.platform == "win32":
            _notify(status_callback, f"Tamanho ctypes INPUT: {ctypes.sizeof(INPUT)}")

        for index, character in enumerate(text, start=1):
            ensure_not_cancelled(cancel_event)
            _notify(
                status_callback,
                f"Digitando caractere {index}/{len(text)}: {character!r}",
            )
            _type_character(character, status_callback)
            if interval_seconds > 0:
                _sleep_with_cancel(interval_seconds, cancel_event)
    except pyautogui.FailSafeException as exc:
        raise TypingCancelled(
            "Digitacao cancelada pelo mecanismo de seguranca do mouse."
        ) from exc
    except TypingCancelled:
        raise
    except Exception:
        _notify(status_callback, traceback.format_exc())
        raise


def _notify(status_callback: Callable[[str], None] | None, message: str) -> None:
    if status_callback is not None:
        status_callback(message)


def _type_character(
    character: str,
    status_callback: Callable[[str], None] | None = None,
) -> None:
    if character == "\n":
        pyautogui.press("enter")
        return

    if character == "\t":
        pyautogui.press("tab")
        return

    if character == " ":
        pyautogui.press("space")
        return

    if _is_printable_ascii(character):
        pyautogui.write(character, interval=0)
        return

    if sys.platform == "win32":
        _notify(status_callback, f"Usando envio Unicode para caractere: {character!r}")
        _send_unicode_character_windows(character, status_callback)
        return

    pyautogui.write(character, interval=0)


def _is_printable_ascii(character: str) -> bool:
    return len(character) == 1 and 32 <= ord(character) <= 126


def _send_unicode_character_windows(
    character: str,
    status_callback: Callable[[str], None] | None = None,
) -> None:
    encoded_character = character.encode("utf-16-le")
    units = [
        int.from_bytes(encoded_character[index : index + 2], "little")
        for index in range(0, len(encoded_character), 2)
    ]

    for unit in units:
        try:
            _send_unicode_key_event(unit, key_up=False)
            _send_unicode_key_event(unit, key_up=True)
        except OSError as exc:
            _notify(
                status_callback,
                (
                    "Falha no envio Unicode. "
                    f"Caractere: {character!r}; "
                    f"codigo Unicode: U+{ord(character):04X}; "
                    f"unidade UTF-16: 0x{unit:04X}; "
                    f"tamanho de INPUT: {ctypes.sizeof(INPUT)}; "
                    f"erro: {exc!r}"
                ),
            )
            raise


def _send_unicode_key_event(code_unit: int, key_up: bool) -> None:
    flags = KEYEVENTF_UNICODE
    if key_up:
        flags |= KEYEVENTF_KEYUP

    input_event = INPUT(
        type=INPUT_KEYBOARD,
        union=INPUT_UNION(
            ki=KEYBDINPUT(
                wVk=0,
                wScan=code_unit,
                dwFlags=flags,
                time=0,
                dwExtraInfo=0,
            )
        ),
    )

    if user32 is None:
        raise OSError("SendInput Unicode esta disponivel apenas no Windows.")

    sent = user32.SendInput(1, ctypes.byref(input_event), ctypes.sizeof(INPUT))
    if sent != 1:
        error_code = ctypes.get_last_error()
        raise OSError(
            f"SendInput falhou: {ctypes.WinError(error_code)}; "
            f"code_unit=0x{code_unit:04X}; "
            f"key_up={key_up}; "
            f"sizeof(INPUT)={ctypes.sizeof(INPUT)}"
        )


class MOUSEINPUT(ctypes.Structure):
    _fields_ = [
        ("dx", wintypes.LONG),
        ("dy", wintypes.LONG),
        ("mouseData", wintypes.DWORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", ULONG_PTR),
    ]


class KEYBDINPUT(ctypes.Structure):
    _fields_ = [
        ("wVk", wintypes.WORD),
        ("wScan", wintypes.WORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", ULONG_PTR),
    ]


class HARDWAREINPUT(ctypes.Structure):
    _fields_ = [
        ("uMsg", wintypes.DWORD),
        ("wParamL", wintypes.WORD),
        ("wParamH", wintypes.WORD),
    ]


class INPUT_UNION(ctypes.Union):
    _fields_ = [
        ("mi", MOUSEINPUT),
        ("ki", KEYBDINPUT),
        ("hi", HARDWAREINPUT),
    ]


class INPUT(ctypes.Structure):
    _fields_ = [
        ("type", wintypes.DWORD),
        ("union", INPUT_UNION),
    ]


LPINPUT = ctypes.POINTER(INPUT)

if user32 is not None:
    user32.SendInput.argtypes = (wintypes.UINT, LPINPUT, ctypes.c_int)
    user32.SendInput.restype = wintypes.UINT
