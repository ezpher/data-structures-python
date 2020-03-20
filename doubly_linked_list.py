class Node():
    
    def __init__(self, data):
            self.data = data
            self._prev = None
            self._next = None

class DoublyLinkedList():
    
    '''instantiates an empty linked list'''
    def __init__(self):
        self._size = 0
        self._head = None
        self._tail = None
    
    '''returns current size of linked list'''
    def size(self):
        return self._size

    '''check if linked list has nodes'''
    def isEmpty(self):
        return self._size == 0

    '''removes nodes from linked list'''
    '''assuming that memory management is necessary'''
    def clear(self):
        current_node = self._head
        while current_node != None:
            next_node = current_node._next
            current_node._prev = current_node._next = None
            current_node = next_node
        self._head = self._tail = None
        self._size = 0

    '''add node to back of linked list by default'''
    def add(self, node):
        self.addLast(node)        
        
    '''add node to back of linked list'''
    def addLast(self, node):
        if self.isEmpty():            
            self._head = self._tail = node
        else:
            node._prev = self._tail
            self._tail._next = node            
            self._tail = node
        self._size += 1

    '''add node to front of linked list'''
    def addFirst(self, node):
        if self.isEmpty():
            self._head = self._tail = node
        else:
            node._next = self._head
            self._head._prev = node
            self._head = node
        self._size += 1

    '''get head's data'''
    def peekFirst(self):        
        if self.isEmpty():
            raise Exception('doubly-linked list is empty')
        else:
            return self._head.data

    '''get tail's data'''
    def peekLast(self):        
        if self.isEmpty():
            raise Exception('doubly-linked list is empty')
        else:
            return self._tail.data

    '''remove first node and get its data'''
    def removeFirst(self):
        if self.isEmpty():
            raise Exception('doubly-linked list is empty')
        
        # TODO: need to clear additional memory as well? e.g. data

        data = self._head.data  # for returning data later
        self._head = self._head._next        
        self._size -= 1

        if self.isEmpty():
            self._tail = self._head # since self._head is None
        else: # for clearing memory; if empty, no need to clear, since no more reference to any nodes at all
            self._head._prev = None 

        return data

    '''remove last node and get its data'''
    def removeLast(self):
        if self.isEmpty():
            raise Exception('doubly-linked list is empty')  

        # TODO: need to clear additional memory as well? e.g. data

        data = self._tail.data
        self._tail = self._tail._prev
        self._size -= 1

        if self.isEmpty():
            self._head = self._tail
        else:            
            self._tail._next = None

    '''remove arbitrary node'''
    def remove(self, node):
        if node._next == None: 
            return self.removeLast()
        
        if node._prev == None: 
            return self.removeFirst()

        # change node pointers to point to nodes behind it and ahead of it respectively
        node._next._prev = node._prev
        node._prev._next = node._next

        data = node.data

        # clear memory
        node.data = None
        node._prev = node._next = None

        self._size -= 1

        return data

    '''remove node at a particular index'''
    def removeAt(self, index):
        if not 0 <= index < self._size:
            raise IndexError('invalid index')
        
        current_node = self._head
        if index < self._size//2: # convert to integer            
            for i in range(self._size//2):
                if i != index:
                    current_node = current_node._next
                else:
                    break
        else:
            for i in range(self._size//2, self._size):
                if i != index:
                    current_node = current_node._next
                else:
                    break
        
        return self.remove(current_node)

    '''remove a particular value in the list'''
    def removeObj(self, obj):
        current_node = self._head
        for i in range(self._size):
            if current_node != None:
                if current_node.data == obj:
                    self.remove(current_node)
                    return True                
                current_node = current_node._next       
        # note in java, should compare separately null and values, since equals on null returns null pointer exception i.e. obj == null vs current_node.data.equals(obj)
        return False

    '''returns index of value if exists in linked list'''
    def indexOf(self, obj):
        current_node = self._head
        for i in range(self._size):
            if current_node != None:
                if current_node.data == obj:
                    return i
                current_node = current_node._next       
        return -1

    '''check if value exists in linked list'''
    def contains(self, obj):
        return self.indexOf(obj) != -1

    '''returns string representation of linked list'''
    def toString(self):   
        current_node = self._head
        list_string = '['
        
        for index in range(self._size):            
            if current_node != None:
                if index != self._size:
                    list_string += current_node.data + "->"
                if index != self._size-1:
                    current_node = current_node._next
                    
        list_string += ']'                    
        return list_string


'''TESTING'''
'''
print('1) Testing size, isEmpty, peekFirst(), peekLast(), add() \n------------------------------\n')
dllist = DoublyLinkedList()
print(dllist.size()) # 0
print(dllist.isEmpty()) # True
# print(dllist.peekFirst()) # 'doubly-linked list is empty' error
# print(dllist.peekLast()) # 'doubly-linked list is empty' error

new_node = Node('Hello')
dllist.add(new_node)
print(dllist._head) # same object as tail
print(dllist._tail) # same object as head
print(dllist.size()) # 1
print(dllist._head.data) # Hello
print(dllist.isEmpty()) # False
print(dllist.peekFirst()) # same as peekLast
print(dllist.peekLast()) # same as peekFirst

new_node = Node('Fellow')
dllist.add(new_node)
print(dllist._head) # different object from tail
print(dllist._tail) # different object from head
print(dllist.size()) # 2
print(dllist._tail.data) # Fellow
print(dllist.isEmpty()) # False
print(dllist.peekFirst()) # different from peekLast
print(dllist.peekLast()) # different from peekFirst

new_node = Node('Coders')
dllist.add(new_node)
print(dllist._head) # different object from tail
print(dllist._tail) # different object from head
print(dllist.size()) # 3
print(dllist._tail.data) # Coders
print(dllist.isEmpty()) # False
print(dllist.peekFirst()) # different from peekLast
print(dllist.peekLast()) # different from peekFirst
print('\n')

print('2) Testing removeFirst() and addFirst() \n------------------------------\n')
dllist.removeFirst()
print(dllist._head.data) # Fellow instead of Hello
print(dllist.size()) # 2

new_node = Node('Forgot')
dllist.addFirst(new_node)
print(dllist._head.data) # Forgot
print(dllist.size()) # 3
new_node = Node('About AddFirst')
dllist.addFirst(new_node)
print(dllist._head.data) # About AddFirst
print(dllist.size()) # 4
dllist.removeFirst()
dllist.removeFirst()

dllist.removeFirst()
print(dllist._head.data) # Coders instead of Fellow
print(dllist.size()) # 1
print('\n')

print('3) Testing removeLast() and error messages for removeFirst() and removeLast() \n------------------------------\n')
new_node = Node('Are The')
dllist.add(new_node)
new_node = Node('Best')
dllist.add(new_node)
dllist.removeLast()
print(dllist._head.data) # Coders
print(dllist.size()) # 2
dllist.removeLast()
print(dllist._head.data) # Coders
print(dllist.size()) # 1

# dllist.removeLast()
# dllist.removeLast() # should throw exception
# dllist.removeFirst() # should throw exception
print('\n')

print('4) Testing remove() \n------------------------------\n')
new_node = Node('Are The')
new_node2 = Node('Best')
new_node3 = Node('In The World')
dllist.add(new_node)
dllist.add(new_node2)
dllist.add(new_node3)
dllist.remove(new_node2)
print(dllist._head._next._next.data) # In The World
print(dllist._head._next.data) # Are The
print(dllist.size()) # 3

dllist.remove(new_node)
print(dllist._head.data) # Coders
print(dllist._head._next.data) # In The World
print(dllist.size()) # 2

print('\n')

print('5) Testing removeAt(), removeObj(), indexOf(), clear(), contains() \n------------------------------\n')
new_node = Node('There Are Many')
dllist.addFirst(new_node)
dllist.removeAt(1)
print(dllist._head.data) # Coders
print(dllist._head._next.data) # In The World
print(dllist.size()) # 2

new_node = Node('In The World')
dllist.addLast(new_node)
print(dllist.removeObj('In The World')) # True
print(dllist.size()) # 2
print(dllist.removeObj('Object Removed')) # False
print(dllist.size()) # 2
print(dllist.contains('In The World')) # True

print(dllist.indexOf('In The World')) # 1
dllist.clear()
print(dllist._head) # None
print(dllist._tail) # None
print(dllist.size()) # 0
print(dllist.indexOf('In The World')) # -1
print(dllist.contains('In The World')) # False

print('\n')

print('6) Testing toString() \n------------------------------\n')
print(dllist.toString()) # []
new_node = Node('test')
new_node2 = Node('test')
new_node3 = Node('test')
dllist.add(new_node)
dllist.add(new_node2)
dllist.add(new_node3)
print(dllist.toString()) # [Test->Test->Test->]
'''










                    


        






