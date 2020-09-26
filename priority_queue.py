
'''implementation of priority queue using a binary min heap'''
class BinaryHeap():
    
    def __init__(self, size = None, collection = None):
        self._heapSize = 0 # The number of elements currently inside the heap; also represents the index for the next element to be added to heap
        self._heapCapacity = 0 # The internal capacity of the heap
        self._heap = None # A dynamic list to track the elements inside the heap        

        '''first overload: if size is provided, instantiate heap with the provided size'''
        if size != None: 
            self._heap = [None] * size        

        '''
        second overload, if non-empty list is provided, instantiate heap with collection size and add each list elem
        , O(nlog(n))
        '''
        if type(collection) is list and len(collection) > 1:
            self._heap = [None] * len(collection)            
            for elem in collection:
                self.add(elem)
    
    '''Returns true/false depending on if the priority queue is empty'''
    def isEmpty(self):
        return self._heapSize == 0
    
    '''Clears everything inside the heap, O(n)'''
    def clear(self):
        for index in range(self._heapCapacity):
            self._heap[index] = None
        self._heapSize = 0
    
    '''Return the size of the heap'''
    def size(self):
        return self._heapSize

    '''
    Returns the value of the element with the lowest
    priority in this priority queue. If the priority
    queue is empty null is returned.
    '''
    def peek(self):
        if self.isEmpty(): 
            raise Exception('heap is empty')
        return self._heap[0]

    '''check if element is in heap, O(n)'''
    def contains(self, elem):
        for index in range(self._heapSize):
            if self._heap == elem:
                return True
        return False

    '''Removes the root of the heap, O(log(n))'''
    def dequeue(self):
        return self.removeAt(0)

    '''
    Adds an element to the priority queue, O(log(n))
    '''
    def enqueue(self, elem):
        if elem == None:
            raise Exception('cannot add null to heap')
        
        if self._heapSize < self._heapCapacity: # i.e. after an element has been removed, and enqueue is called
            self._heap[self._heapSize] = elem
        else: # i.e. adding new elements
            self._heap.append(elem)
            self._heapCapacity += 1

        self.swim(self._heapSize)
        self._heapSize += 1    

    '''Removes a node at particular index, O(log(n))'''
    def removeAt(self, index):
        if self.isEmpty():
            raise Exception('cannot add null to heap')

        self._heapSize -= 1
        removed_data = self._heap[index]
        self.swap(index, self._heapSize)

        '''Remove the value'''
        self._heap[self._heapSize] = None

        '''Check if the last element was removed'''
        if index == self._heapSize: 
            return removed_data
        
        elem = self._heap[index]

        '''naive method of checking whether to sink or swim i.e. just try both'''
        '''Try sinking element'''
        self.sink(index)

        '''if sinking did not work try swimming'''
        if self._heap[index] == elem: 
            self.swim(index)

        return removed_data

    '''perform node swim upstream if heap invariant not met, O(log n)'''
    def swim(self, index):

        '''Grab the index of the immediate parent node relative to index'''
        '''works for both left and right node'''
        parent = (index - 1) // 2 # round down to nearest integer

        '''Keep swimming while we have not reached the'''
        '''root and while we're less than our parent.'''
        while index > 0 and self.less(index, parent):
            self.swap(parent, index)
            index = parent # now parent becomes the new index                    
            parent = (index - 1) // 2 # Grab the index of the next parent node relative to index

    '''perform node sink downstream if heap invariant not met, O(log n)'''
    def sink(self, index):
        while True:
            left = (2 * index) + 1 # Left  node
            right = (2 * index) + 2 # Right node
            smallest = left; # Assume left is the smallest node of the two children first

            '''Find which is smaller left or right'''
            '''If right is smaller set smallest to be right'''
            if right < self._heapSize and self.less(right, left): 
                smallest = right

            '''Stop if we're outside the bounds of the tree'''
            '''or stop early if we cannot sink k anymore'''
            if left >= self._heapSize or self.less(index, smallest):
                break

            '''Move down the tree following the smallest node'''
            self.swap(smallest, index)
            index = smallest    

    '''
    tests if value of node_i is less or equal to node_j
    assumes that i and j indices are valid, O(1)    
    '''
    def less(self, iIndex, jIndex):
        elem_i = self._heap[iIndex]
        elem_j = self._heap[jIndex]

        if elem_i <= elem_j:
            return True

        return False

    ''''Swap two nodes. Assumes indices i & j are valid, O(1)'''
    def swap(self, iIndex, jIndex):
        elem_i = self._heap[iIndex]
        elem_j = self._heap[jIndex]

        self._heap[iIndex] = elem_j
        self._heap[jIndex] = elem_i

    def toString(self):
        if self.isEmpty():
            return '[]'
        return ','.join(self._heap)
    





    

    


