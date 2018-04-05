class Queue:
    def __init__(self):
        self.array = []
    
    def add(self, item):
        self.array.insert(0, item)
    
    def remove(self):
        return self.array.pop(len(self.array)-1)

    def peek(self):
        ret = None
        if len(self.array) > 0:
            ret = self.array[len(self.array)-1]
        return ret
