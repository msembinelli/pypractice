class Stack:
    def __init__(self):
        self.array = []
    
    def push(self, item):
        self.array.insert(0, item)
    
    def pop(self):
        ret = None
        if len(self.array) > 0:
            ret = self.array.pop(0)
        return ret

    def peek(self):
        ret = None
        if len(self.array) > 0:
            ret = self.array[0]
        return ret
