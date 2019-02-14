from py_min_stack import stack

class Queue:
    def __init__(self):
        self.deque_stack = stack.Stack()
        self.enqueue_stack = stack.Stack()

    def enqueue(self, item):
        self.enqueue_stack.push(item)

    def deque(self):
        if (not self.enqueue_stack) and (not self.deque_stack):
            raise IndexError
        elif not self.deque_stack:
            while self.enqueue_stack:
                self.deque_stack.push(self.enqueue_stack.pop())
        return self.deque_stack.pop()

    def find_min(self):
        return min(self.enqueue_stack.find_min(), self.deque_stack.find_min())

    def __len__(self):
        return len(self.enqueue_stack + self.deque_stack)