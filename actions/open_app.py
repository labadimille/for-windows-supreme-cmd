import os
import subprocess
import sys


def open_app(name: str):
    """Open an application or URL by name. On Windows uses `os.startfile` when possible,
    otherwise tries subprocess.
    """
    name = name or ''
    print(f"[ACTION] Request to open: {name}")
    try:
        # If looks like a URL, open in browser
        if name.startswith('http://') or name.startswith('https://'):
            import webbrowser

            webbrowser.open(name)
            return True

        # On Windows, os.startfile can open apps or files registered with the system
        if sys.platform.startswith('win'):
            try:
                os.startfile(name)
                return True
            except OSError:
                # Fall back to start via cmd
                subprocess.Popen(['start', name], shell=True)
                return True

        # On macOS, try the `open` command
        if sys.platform == 'darwin':
            subprocess.Popen(['open', name])
            return True

        # On Linux, try xdg-open
        subprocess.Popen(['xdg-open', name])
        return True
    except Exception as e:
        print(f"[ACTION] Failed to open {name}: {e}")
        return False
