class Stack:
    def __init__ (self):
        self.elements = []

    def is_empty(self):
        return self.elements == []

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        return self.elements.pop()

    def peek(self):
        return self.elements[-1]

    def size(self):
        return len(self.elements)
