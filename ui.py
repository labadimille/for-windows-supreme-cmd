# Minimal UI stub for compatibility with expanded main

class JarvisUI:
    def __init__(self):
        print('[UI] Minimal JarvisUI initialized')

    def start(self):
        print('[UI] start called (minimal)')

    def stop(self):
        print('[UI] stop called (minimal)')

    def show_message(self, title, body):
        print(f'[UI] {title}: {body}')
