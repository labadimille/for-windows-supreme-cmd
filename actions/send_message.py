import webbrowser
from urllib.parse import quote_plus
from datetime import datetime


def send_message(target: str, message: str):
    """Send or log a message.

    This function appends the message to `messages.log` and opens the default
    mail client with a `mailto:` link as a convenience.
    """
    target = target or 'unknown'
    message = message or ''
    timestamp = datetime.utcnow().isoformat()
    log_line = f"{timestamp} | {target} | {message}\n"
    try:
        with open('messages.log', 'a', encoding='utf-8') as f:
            f.write(log_line)
        print(f"[ACTION] Logged message to messages.log: {log_line.strip()}")
    except Exception as e:
        print(f"[ACTION] Failed to log message: {e}")

    # Open mail client as convenience (will fail silently if not configured)
    try:
        mailto = f"mailto:{quote_plus(target)}?body={quote_plus(message)}"
        webbrowser.open(mailto)
    except Exception:
        pass
    return True
