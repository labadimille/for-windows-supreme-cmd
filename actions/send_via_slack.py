import json
from pathlib import Path
try:
    import requests
except Exception:
    requests = None


def _load_slack_config():
    cfg_path = Path('config') / 'api_keys.json'
    if cfg_path.exists():
        try:
            with open(cfg_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get('slack')
        except Exception:
            return None
    return None


def send_via_slack(channel: str, message: str, webhook_url: str = None) -> bool:
    """Send a Slack message via Incoming Webhook (webhook_url) or via API token.

    If webhook_url not provided, reads config/api_keys.json -> slack.webhook_url
    """
    channel = channel or ''
    message = message or ''
    cfg = {'webhook_url': webhook_url} if webhook_url else _load_slack_config()
    if not cfg or not cfg.get('webhook_url'):
        print('[Slack] No webhook_url configured (config/api_keys.json -> slack.webhook_url).')
        return False
    if not requests:
        print('[Slack] requests library not available. Install with `pip install requests`.')
        return False

    url = cfg.get('webhook_url')
    payload = {'text': message}
    try:
        r = requests.post(url, json=payload, timeout=10)
        if r.ok:
            print('[Slack] Message posted')
            return True
        else:
            print(f'[Slack] Failed: {r.status_code} {r.text}')
            return False
    except Exception as e:
        print(f'[Slack] Exception: {e}')
        return False
