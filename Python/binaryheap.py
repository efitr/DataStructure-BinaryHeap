# ----------------------------------------------------------
# ----------------------------------------------------------
# BinaryHeap DataStructure implemented on Python3.
# ----------------------------------------------------------
# ----------------------------------------------------------

# Components:
'''
    The python3 programming language.
    A python3 class, an object oriented approach towards programming.
    A python3 list AbstractDataType.
'''

# ----------------------------------------------------------
# Class BinaryMinHeap
# ----------------------------------------------------------
class BinaryMinHeap(object):
    """BinaryMinHeap: a partially ordered collection with efficient methods to
    insert new items in partial order and to access and remove its minimum item.
    Items are stored in a dynamic array that implicitly represents a complete
    binary tree with root node at index 0 and last leaf node at index n-1."""

    # Make initializer ( self , items=None )
    def __init__(self, items=None):
        self.binaryheap = []
        self.lenght = 0
        for item in items:
            self.binaryheap.append(item)
            self.lenght += 1

    # Helper function is empty ( self )
    def is_empty(self):
        if self.binaryheap is []:
            return True
        return False

    # Size function ( self )
    def size(self):
        return self.lenght

    # Function get minimun item ( self )
    def get_minimun_item(self):
        pass

    # Delete minimun item function ( self )
    def delete_minimun_item(self):
        pass

    # Function replace minimun item ( self , item )
    def replace_minimun_item(self, item):
        pass

    # Function bubble up ( self , index )
    def bubble_up(self, index):
        pass

    # Function bubble down ( self , index )
    def buble_down(self, index):
        pass

    # Function last index ( self )
    def last_index(self):
        pass

    # Function parent index ( self , index )
    def parent_index(self, index):
        return (index-1)/2

    # Function left child index ( self , index )
    def left_child_index(self, index):
        return (index * 2) + 1

    # Function right child index ( self , index )
    def right_child_index(self, index):
        return (index * 2) + 2

# ----------------------------------------------------------
# Class BinaryMaxHeap
# ----------------------------------------------------------

class BinaryMaxHeap(object):
    """BinaryMaxHeap: a partially ordered collection with efficient methods to
    insert new items in partial order and to access and remove its maximun item.
    Items are stored in a dynamic array that implicitly represents a complete
    binary tree with root node at index 0 and last leaf node at index n-1."""

    pass
