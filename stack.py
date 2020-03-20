from doubly_linked_list import DoublyLinkedList as DLL
from doubly_linked_list import Node 

class Stack():
    def __init__(self, node=None):
        self._list = DLL()

        if node != None:
            self.push(node)

    def size(self):
        return self._list.size()

    def isEmpty(self):
        return self.size() == 0

    def push(self, node):
        self._list.addLast(node)

    def pop(self):
        if self.isEmpty():
            raise Exception('stack is empty')
        return self._list.removeLast()

    def peek(self):
        if self.isEmpty():
            raise Exception('stack is empty')
        return self._list.peekLast()


'''TESTING'''        
stack = Stack()
print(stack.isEmpty()) # True
print(stack.size()) # 0
# print(stack.pop()) # should throw error
# print(stack.peek()) # should throw error

node = Node('Test')
stack = Stack(node) 
print(stack._list._head.data) # Test
print(stack.isEmpty()) # False
print(stack.size()) # 1
print(stack.peek()) # Test
stack.pop()
print(stack.size()) # 0


