import smtplib
from email.message import EmailMessage
import json
from pathlib import Path


def _load_smtp_config():
    cfg_path = Path('config') / 'api_keys.json'
    if cfg_path.exists():
        try:
            with open(cfg_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get('smtp') or data
        except Exception:
            return None
    return None


def send_via_smtp(recipient: str, subject: str, body: str, smtp_config: dict = None) -> bool:
    """Send an email via SMTP. smtp_config should contain host, port, username, password, use_tls.

    If no smtp_config provided, attempts to read `config/api_keys.json` -> ['smtp'].
    Returns True on success, False otherwise.
    """
    recipient = recipient or ''
    subject = subject or ''
    body = body or ''

    cfg = smtp_config or _load_smtp_config()
    if not cfg:
        print('[SMTP] No SMTP configuration found (config/api_keys.json missing or empty).')
        return False

    host = cfg.get('host')
    port = cfg.get('port', 587)
    username = cfg.get('username')
    password = cfg.get('password')
    use_tls = cfg.get('use_tls', True)

    if not host or not username or not password:
        print('[SMTP] Incomplete SMTP configuration; need host, username, password.')
        return False

    msg = EmailMessage()
    msg['From'] = username
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.set_content(body)

    try:
        if use_tls:
            s = smtplib.SMTP(host, port, timeout=10)
            s.starttls()
        else:
            s = smtplib.SMTP(host, port, timeout=10)
        s.login(username, password)
        s.send_message(msg)
        s.quit()
        print(f'[SMTP] Sent email to {recipient}')
        return True
    except Exception as e:
        print(f'[SMTP] Failed to send email: {e}')
        return False
