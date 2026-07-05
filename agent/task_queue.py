class TaskQueue:
    def __init__(self):
        self.queue = []

    def add(self, task):
        self.queue.append(task)
        print(f'[AGENT] Task added: {task}')

    def pop(self):
        if self.queue:
            return self.queue.pop(0)
        return None
