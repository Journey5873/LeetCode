class MyQueue():

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, x):
        self.inStack.append(x)
        return None

    def pop(self):
        if not self.outStack:
            while self.inStack:
                value = self.inStack.pop()
                self.outStack.append(value)
        return self.outStack.pop()

    def peek(self):
        if not self.outStack:
            while self.inStack:
                value = self.inStack.pop()
                self.outStack.append(value)
        return self.outStack[-1]

    def empty(self):
        return len(self.inStack) == 0 and len(self.outStack) == 0