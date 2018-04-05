class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class Linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next
    
    def insert_first(self, node):
        saved = self.head
        self.head = node
        self.head.next = saved
        self.size += 1
    
    def get_first(self):
        return self.head
    
    def remove_first(self):
        node = None
        if self.head is not None:
            node = self.head
            self.head = self.head.next
            self.size -= 1
        return node

    def insert_last(self, node):
        if self.head is None:
            self.head = node
        else:
            i_node = self.head
            while i_node.next != None:
                i_node = i_node.next
            i_node.next = node
        self.size += 1
    
    def get_last(self):
        i_node = None
        if self.head is not None:
            i_node = self.head
            while i_node.next != None:
                i_node = i_node.next
        return i_node
    
    def remove_last(self):
        node = None
        if self.head is not None:
            if self.head.next is not None:
                i_node = self.head
                while i_node.next.next is not None:
                    i_node = i_node.next
                node = i_node.next
                i_node.next = None
            else:
                node = self.head
                self.head = None
            self.size -= 1
        return node

    def insert_at(self, index, node):
        if self.head is not None:
            i_node = self.head
            for i in range(0, index):
                if i_node.next is None:
                    break
                i_node = i_node.next
            node.next = i_node.next
            i_node.next = node
        else:
            self.head = node
        self.size += 1

    def get_at(self, index):
        node = None
        if self.head is not None:
            i_node = self.head
            for i in range(0, index):
                if i_node.next is None:
                    break
                i_node = i_node.next
            node = i_node
        return node

    def remove_at(self, index):
        node = None
        if self.head is not None:
            i_node = self.head
            for i in range(0, index):
                i_node = i_node.next
            node = i_node
            i_node = i_node.next
            self.size -= 1
        return node
    
    def clear(self):
        self.__init__()
    
