from collections import deque


class Buffer:

    def __init__(self):
        self.messages = deque()
        self.amount: int = 0

    def empty(self):
        return True if len(self.messages) == 0 else False

    def add(self, msg):
        if msg != '':
            self.messages.append(msg)
            self.amount += 1

    def pop(self):
        self.amount -= 1
        return self.messages.popleft()

    def count(self):
        return self.amount

    def print_info(self):
        print(f"Buffer: {self.messages}")
        print(f"Buffer length = {len(self.messages)}")
