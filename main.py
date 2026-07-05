"""Expanded minimal `main.py` with simple action dispatch.

Provides a small interactive loop with commands:
 - `status` — show status
 - `open <name>` — call `actions.open_app.open_app(name)`
 - `search <query>` — call `actions.web_search.web_search(query)`
 - `send <target> <message>` — call `actions.send_message.send_message(target, message)`
 - `help` — show help
 - `exit` — quit
"""
import sys
import importlib
from ui import JarvisUI


class ActionManager:
    def __init__(self):
        self.actions = {}
        self._load_action_modules()

    def _load_action_modules(self):
        # Dynamically import all modules under the `actions` package
        try:
            import actions as actions_pkg
            import pkgutil
            for finder, name, ispkg in pkgutil.iter_modules(actions_pkg.__path__):
                mod_name = f"actions.{name}"
                try:
                    m = importlib.import_module(mod_name)
                    for attr in dir(m):
                        if attr.startswith('_'):
                            continue
                        fn = getattr(m, attr)
                        if callable(fn):
                            key = f"{m.__name__.split('.')[-1]}.{attr}"
                            self.actions[key] = fn
                except Exception:
                    # ignore individual import errors
                    pass
        except Exception:
            # actions package not available
            pass

    def call(self, name, *args):
        # Provide simple mapping for friendly names
        if name == 'open' and 'open_app.open_app' in self.actions:
            return self.actions['open_app.open_app'](*args)
        if name == 'search' and 'web_search.web_search' in self.actions:
            return self.actions['web_search.web_search'](*args)
        if name == 'send' and 'send_message.send_message' in self.actions:
            return self.actions['send_message.send_message'](*args)
        if name == 'sendsmtp' and 'send_via_smtp.send_via_smtp' in self.actions:
            return self.actions['send_via_smtp.send_via_smtp'](*args)
        if name == 'sendtg' and 'send_via_telegram.send_via_telegram' in self.actions:
            return self.actions['send_via_telegram.send_via_telegram'](*args)
        if name == 'sendslack' and 'send_via_slack.send_via_slack' in self.actions:
            return self.actions['send_via_slack.send_via_slack'](*args)
        if name == 'browse' and 'browser_control.browse' in self.actions:
            return self.actions['browser_control.browse'](*args)
        raise ValueError(f"Unknown action: {name}")


def print_help():
    print("Commands:")
    print("  status")
    print("  open <name>")
    print("  search <query>")
    print("  send <target> <message>")
    print("  help")
    print("  exit")


def main():
    ui = JarvisUI()
    ui.start()

    am = ActionManager()

    print("[JARVIS] Starting expanded runtime...")
    print("[JARVIS] Ready (expanded minimal). Type 'help' for commands.")

    try:
        while True:
            raw = input('> ')
            if not raw:
                continue
            parts = raw.split(' ', 2)
            cmd = parts[0].strip().lower()
            if cmd in ('exit', 'quit'):
                print('[JARVIS] Shutting down.')
                break
            if cmd == 'help':
                print_help()
                continue
            if cmd == 'status':
                print('[JARVIS] All systems nominal (expanded).')
                continue
            if cmd == 'open' and len(parts) >= 2:
                name = parts[1].strip()
                try:
                    am.call('open', name)
                except Exception as e:
                    print(f'[JARVIS] Error calling open: {e}')
                continue
            if cmd == 'browse' and len(parts) >= 2:
                url = parts[1].strip()
                try:
                    am.call('browse', url)
                except Exception as e:
                    print(f'[JARVIS] Error calling browse: {e}')
                continue
            if cmd == 'search' and len(parts) >= 2:
                query = raw.partition(' ')[2]
                try:
                    am.call('search', query)
                except Exception as e:
                    print(f'[JARVIS] Error calling search: {e}')
                continue
            if cmd == 'sendsmtp' and len(parts) >= 2:
                # format: sendsmtp <recipient> <subject> <body>
                rest = raw.partition(' ')[2]
                segs = rest.split(' ', 2)
                if len(segs) < 3:
                    print('[JARVIS] Usage: sendsmtp <recipient> <subject> <body>')
                    continue
                recipient, subject, body = segs[0].strip(), segs[1].strip(), segs[2].strip()
                try:
                    am.call('sendsmtp', recipient, subject, body)
                except Exception as e:
                    print(f'[JARVIS] Error calling sendsmtp: {e}')
                continue
            if cmd == 'sendtg' and len(parts) >= 2:
                rest = raw.partition(' ')[2]
                segs = rest.split(' ', 1)
                if len(segs) < 2:
                    print('[JARVIS] Usage: sendtg <chat_id> <message>')
                    continue
                chat_id, message = segs[0].strip(), segs[1].strip()
                try:
                    am.call('sendtg', chat_id, message)
                except Exception as e:
                    print(f'[JARVIS] Error calling sendtg: {e}')
                continue
            if cmd == 'sendslack' and len(parts) >= 2:
                rest = raw.partition(' ')[2]
                segs = rest.split(' ', 1)
                if len(segs) < 2:
                    print('[JARVIS] Usage: sendslack <channel> <message>')
                    continue
                channel, message = segs[0].strip(), segs[1].strip()
                try:
                    am.call('sendslack', channel, message)
                except Exception as e:
                    print(f'[JARVIS] Error calling sendslack: {e}')
                continue
            if cmd == 'send' and len(parts) >= 3:
                target = parts[1].strip()
                message = parts[2].strip()
                try:
                    am.call('send', target, message)
                except Exception as e:
                    print(f'[JARVIS] Error calling send: {e}')
                continue
            print(f"[JARVIS] Unknown command: {raw}")
    except (KeyboardInterrupt, EOFError):
        print('\n[JARVIS] Interrupted, exiting.')
    finally:
        ui.stop()


if __name__ == '__main__':
    main()
