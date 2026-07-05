import json
from pathlib import Path
try:
    import requests
except Exception:
    requests = None


def _load_telegram_config():
    cfg_path = Path('config') / 'api_keys.json'
    if cfg_path.exists():
        try:
            with open(cfg_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get('telegram')
        except Exception:
            return None
    return None


def send_via_telegram(chat_id: str, message: str, bot_token: str = None) -> bool:
    """Send a Telegram message using Bot API. Requires bot_token and chat_id."""
    chat_id = chat_id or ''
    message = message or ''
    cfg = {'bot_token': bot_token} if bot_token else _load_telegram_config()
    if not cfg or not cfg.get('bot_token'):
        print('[Telegram] No bot token configured (config/api_keys.json -> telegram.bot_token).')
        return False
    if not requests:
        print('[Telegram] requests library not available. Install with `pip install requests`.')
        return False

    token = cfg.get('bot_token')
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    try:
        r = requests.post(url, json={'chat_id': chat_id, 'text': message}, timeout=10)
        if r.ok:
            print('[Telegram] Message sent')
            return True
        else:
            print(f'[Telegram] Failed: {r.status_code} {r.text}')
            return False
    except Exception as e:
        print(f'[Telegram] Exception: {e}')
        return False
