from collections import deque


class Buffer:

    def __init__(self):
        self.messages = deque()

    def empty(self):
        return True if len(self.messages) == 0 else False

    def add(self, msg):
        self.messages.append(msg)

    def get(self):
        return self.messages.popleft()

    def print_info(self):
        print(f"Buffer: {self.messages}")
        print(f"Buffer length = {len(self.messages)}")
