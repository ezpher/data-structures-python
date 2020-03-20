'''using ctypes module raw array, for implementing dynamic array since list in python is already a dynamic array'''
import ctypes 

class DynamicArray():    
    
    '''instantiating new array when class is created'''
    def __init__(self):
        self.length = 0 # size that user sees
        self._capacity = 1 # actual size
        self._array = self._make_array(self._capacity) 

    '''PRIVATE METHODS'''
    '''creating a new array'''
    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()
    
    '''resizing array each time capacity is reached'''
    def _resize(self, new_size):
        temp_array = self._make_array(new_size)
        for i in range(self.length):
            temp_array[i] = self._array[i]
        self._array = temp_array
        self._capacity = new_size   

    '''UTILITY METHODS'''
    '''return current length of array'''
    def __len__(self): 
        return self.length 

    '''find index of first object that matches inputted object'''
    def indexOf(self, obj):
        for index in range(self.length):
            if self._array[index] == obj:
                return index
        return -1

    '''check if array contains object'''
    def contains(self, obj):
        return self.indexOf(obj) != -1        

    '''check array is empty'''
    def isEmpty(self):
        return self.length == 0

    '''clear array of values and reset length i.e. current index to 0'''
    def clear(self):
        for index in range(self.length):
            self._array[index] = 'None' # note that certain ctypes values don't support None as a value, so use 'None'
        self.length = 0

    '''get string representation of array'''
    def __str__(self):
        array_str = '['
        if self.length == 0:
            array_str = '[]'
            return array_str
        else:
            for index in range(self.length):
                if index != self.length-1:
                    array_str += str(self._array[index]) + ', '
                else:
                    array_str += str(self._array[index]) + ']'
            return array_str

    '''getting value at array index'''
    def __getitem__(self, index):
        if not 0 <= index < self.length: # equivalent to (0 <= index) and (index <= self.length)
            raise IndexError('invalid index')
        return self._array[index]

    '''setting value at array index'''
    def __setitem__(self, index, value):
        if not 0 <= index < self.length:
            raise IndexError('invalid index')
        self._array[index] = value       

    '''adding new object to end of array''' 
    '''if array contains no object to begin with, need to instantiate a new Dynamic Array class'''
    def append(self, obj):
        if self.length == self._capacity:
            self._resize(2 * self._capacity) 
        self._array[self.length] = obj
        self.length += 1

    '''remove object at the to-remove index''' 
    def __delitem__(self, rm_index):
        if not 0 <= rm_index < self.length:
            raise IndexError('invalid index')
        
        toRemoveItem = self._array[rm_index] 
        new_array = self._make_array(self.length-1)

        j = -1 # second index to keep track of indexing (excluding rm_index). initialized with -1 since incremented for each iteration of for-loop
        for i in range(self.length):
            j += 1 # for incrementing for each iteration of the for-loop in tandem with i
            if i == rm_index:
                j -= 1  # j will lag behind i if i is the to-remove index
                continue
            else:
                new_array[j] = self._array[i]    

        self._array = new_array
        self.length -= 1
        self._capacity -= 1   
        return toRemoveItem

    '''remove object if matches existing object in array''' 
    def remove(self, obj):
        for index in range(self.length):
            if self._array[index] == obj:
                self.__delitem__(index) 
                return True                
        return False

'''TESTING'''

'''testing append'''
test_array = DynamicArray()
print(len(test_array)) # 0
test_array.append(1)
test_array.append(2)
test_array.append(3)
print(len(test_array)) # 3

'''testing __delitem__'''
print(len(test_array)) # 3
print(test_array.__delitem__(1)) # 2
print(test_array._array._objects) # [1, 3]
print(len(test_array)) # 2

'''testing isEmpty'''
print(test_array.isEmpty()) # False
test_array.__delitem__(0)
test_array.__delitem__(0)
print(test_array.isEmpty()) # True

'''testing __getItem__'''
test_array = DynamicArray()
test_array.append(1)
test_array.append(2)
print(test_array.__getitem__(1)) # 2

'''testing __setItem__'''
test_array.__setitem__(0, 2)
print(test_array.__getitem__(0)) # 2
print(test_array._array._objects) # [2,2]

'''testing clear'''
test_array.clear()
print(test_array._array._objects) # ['None', 'None']
print(test_array.length) # 0
print(test_array._capacity) # 2; capacity remains the same

'''testing remove'''
test_array = DynamicArray()
test_array.append(1)
test_array.append(2)
test_array.append(3)
print(test_array.remove(2)) # True
print(test_array._array._objects) # [1,3]

print(test_array.remove(4)) # False
print(test_array._array._objects) # [1,3]

'''testing indexOf'''
test_array = DynamicArray()
test_array.append(1)
test_array.append(2)
test_array.append(4)
print(test_array.indexOf(4)) # 2

'''testing contains'''
test_array = DynamicArray()
print(test_array.contains(4)) # False
test_array.append(1)
test_array.append(2)
print(test_array.contains(2)) # True

'''testing toString'''
test_array = DynamicArray()
print(test_array.__str__()) # []
test_array.append(1)
test_array.append(2)
test_array.append(3)
print(test_array.__str__()) # [1, 2, 3]






















    