'''This is the implementation of the stack class.
I added two additional functions, size() for getting the size of the stack
and repr() for printing the stack.
'''


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def __repr__(self):
        return repr(self.stack)  # For easier debugging
