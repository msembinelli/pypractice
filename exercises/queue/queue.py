class Queue:
    def __init__(self):
        self.array = []
    
    def add(self, item):
        self.array.insert(0, item)
    
    def remove(self):
        return self.array.pop(len(self.array)-1)
