TRANSLATIONS = {
    "pt": {
        "app_title": "MLI-Knot Keyboard",
        "instruction": (
            "Cole ou digite o texto abaixo. Após iniciar, clique no campo de "
            "destino antes da contagem terminar."
        ),
        "initial_delay": "Atraso inicial (segundos):",
        "character_interval": "Intervalo entre caracteres:",
        "start": "Iniciar digitação",
        "cancel": "Cancelar",
        "quick_test": "Teste rápido",
        "language": "English",
        "status": "Status",
        "ready": "Pronto.",
        "ready_log": "Pronto. Cole ou digite o texto com acentos na caixa acima.",
        "empty_title": "Texto vazio",
        "empty_message": "Informe o texto a ser digitado.",
        "invalid_title": "Valor inválido",
        "confirm_title": "Confirmar digitação",
        "confirm_message": (
            "Após confirmar, clique no campo de destino durante a contagem "
            "regressiva.\n\nDeseja iniciar?"
        ),
        "quick_confirm_message": (
            "Teste rápido: após confirmar, clique no Bloco de Notas durante a "
            "contagem regressiva.\n\nDeseja iniciar?"
        ),
        "cancelled_before_start": "Operação cancelada antes do início.",
        "quick_started": "Teste rápido iniciado. Digitará abc123 após 5 segundos.",
        "countdown_started": "Contagem regressiva iniciada.",
        "click_target": "Clique no campo de destino agora.",
        "typing_started": "Digitação iniciada.",
        "typing_done": "Digitação concluída com sucesso.",
        "unexpected_error": "Erro inesperado:",
        "cancel_requested": "Cancelamento solicitado.",
        "running": "Executando...",
        "field_number": "Informe um número válido para {field_name}.",
        "minimum": "O valor mínimo para {field_name} é {minimum}.",
        "maximum": "O valor máximo para {field_name} é {maximum}.",
        "initial_delay_name": "atraso inicial",
        "character_interval_name": "intervalo entre caracteres",
    },
    "en": {
        "app_title": "MLI-Knot Keyboard",
        "instruction": (
            "Paste or type the text below. After starting, click the target "
            "field before the countdown ends."
        ),
        "initial_delay": "Initial delay (seconds):",
        "character_interval": "Character interval:",
        "start": "Start typing",
        "cancel": "Cancel",
        "quick_test": "Quick test",
        "language": "Português",
        "status": "Status",
        "ready": "Ready.",
        "ready_log": "Ready. Paste or type text with accents in the box above.",
        "empty_title": "Empty text",
        "empty_message": "Enter the text to type.",
        "invalid_title": "Invalid value",
        "confirm_title": "Confirm typing",
        "confirm_message": (
            "After confirming, click the target field during the countdown.\n\n"
            "Start now?"
        ),
        "quick_confirm_message": (
            "Quick test: after confirming, click Notepad during the countdown.\n\n"
            "Start now?"
        ),
        "cancelled_before_start": "Operation cancelled before start.",
        "quick_started": "Quick test started. It will type abc123 after 5 seconds.",
        "countdown_started": "Countdown started.",
        "click_target": "Click the target field now.",
        "typing_started": "Typing started.",
        "typing_done": "Typing completed successfully.",
        "unexpected_error": "Unexpected error:",
        "cancel_requested": "Cancellation requested.",
        "running": "Running...",
        "field_number": "Enter a valid number for {field_name}.",
        "minimum": "The minimum value for {field_name} is {minimum}.",
        "maximum": "The maximum value for {field_name} is {maximum}.",
        "initial_delay_name": "initial delay",
        "character_interval_name": "character interval",
    },
}


def translate(language: str, key: str) -> str:
    return TRANSLATIONS.get(language, TRANSLATIONS["pt"]).get(key, key)
