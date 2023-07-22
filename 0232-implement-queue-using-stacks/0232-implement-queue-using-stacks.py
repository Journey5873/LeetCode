class MyQueue():

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, x):
        self.inStack.append(x)
        return None

    def pop(self):
        self.peek()
        return self.outStack.pop()

    def peek(self):
        if not self.outStack:
            i = 0
            lenght = len(self.inStack)
            while i in range (0, lenght):
                value = self.inStack.pop()
                self.outStack.append(value)
                i += 1
        return self.outStack[-1]

    def empty(self):
        if len(self.inStack) == 0 and len(self.outStack) == 0:
            return True
        else:
            return False