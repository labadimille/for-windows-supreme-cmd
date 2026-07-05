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
        # Try to import known action modules; missing ones are ignored
        modules = [
            'actions.open_app',
            'actions.web_search',
            'actions.send_message',
        ]
        for mod in modules:
            try:
                m = importlib.import_module(mod)
                for attr in dir(m):
                    if attr.startswith('_'):
                        continue
                    fn = getattr(m, attr)
                    if callable(fn):
                        key = f"{m.__name__.split('.')[-1]}.{attr}"
                        self.actions[key] = fn
            except Exception:
                # module not available — skip
                pass

    def call(self, name, *args):
        # Provide simple mapping for friendly names
        if name == 'open' and 'open_app.open_app' in self.actions:
            return self.actions['open_app.open_app'](*args)
        if name == 'search' and 'web_search.web_search' in self.actions:
            return self.actions['web_search.web_search'](*args)
        if name == 'send' and 'send_message.send_message' in self.actions:
            return self.actions['send_message.send_message'](*args)
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

    print("[JARVIS] 🔌 Starting expanded runtime...")
    print("[JARVIS] ✅ Ready (expanded minimal). Type 'help' for commands.")

    try:
        while True:
            raw = input('> ')
            if not raw:
                continue
            parts = raw.split(' ', 2)
            cmd = parts[0].strip().lower()
            if cmd in ('exit', 'quit'):
                print('[JARVIS] 👋 Shutting down.')
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
            if cmd == 'search' and len(parts) >= 2:
                query = raw.partition(' ')[2]
                try:
                    am.call('search', query)
                except Exception as e:
                    print(f'[JARVIS] Error calling search: {e}')
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
        print('\n[JARVIS] 👋 Interrupted, exiting.')
    finally:
        ui.stop()


if __name__ == '__main__':
    main()
