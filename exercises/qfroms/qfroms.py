from stack import Stack
class Qfroms:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()
    
    def add(self, item):
        self.in_stack.push(item)
    
    def remove(self):
        return self.__out_helper(self.out_stack.pop)

    def peek(self):
        return self.__out_helper(self.out_stack.peek)
    
    def __out_helper(self, func):
        while self.in_stack.peek() is not None:
            self.out_stack.push(self.in_stack.pop())
        ret = func()
        while self.out_stack.peek() is not None:
            self.in_stack.push(self.out_stack.pop())
        return ret
