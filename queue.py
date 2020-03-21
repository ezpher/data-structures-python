from doubly_linked_list import DoublyLinkedList as DLL, Node

class Queue():

    def __init__(self, node=None):
        self._list = DLL()
        if node != None:
            self.enqueue(node)
    
    def size(self):
        return self._list.size()

    def isEmpty(self):
        return self._list.size() == 0

    def peek(self):
        if self.isEmpty():
            raise Exception('queue is empty')
        return self._list.peekFirst()

    def enqueue(self, node):
        self._list.addLast(node)

    def dequeue(self):
        if self.isEmpty():
            raise Exception('queue is empty')
        return self._list.removeFirst()

'''TESTING'''

queue = Queue()
print(queue.isEmpty()) # True
print(queue.size()) # 0
# print(queue.peek()) # should throw error
# print(queue.dequeue()) # should throw error

node = Node('Test')
node2 = Node('Test2')
queue = Queue(node)
queue.enqueue(node2)
print(queue.isEmpty()) # False
print(queue.size()) # 2
print(queue.peek()) # Test
print(queue.dequeue()) # Test



        
