# datastructures.array.Array

""" This module defines an Array class that represents a one-dimensional array. 
    See the stipulations in iarray.py for more information on the methods and their expected behavior.
    Methods that are not implemented raise a NotImplementedError until they are implemented.
"""

from __future__ import annotations
from collections.abc import Sequence
import os
from typing import Any, Iterator, overload
import numpy as np
import copy


from datastructures.iarray import IArray, T


class Array(IArray[T]):  

    def __init__(self, starting_sequence: Sequence[T]=[], data_type: type=object) -> None: 
        if not isinstance(starting_sequence, Sequence):
            raise ValueError("starting_sequence must be a sequence type (e.g., list, tuple).")
        if not all(isinstance(item, data_type) for item in starting_sequence):
            raise TypeError(f"All elements in starting_sequence must be of type {data_type.__name__}.")
        self.data_type = data_type
        self.logical_size = len(starting_sequence)  
        self.physical_size = max(10, self.logical_size * 2)  

        # Initialize NumPy array with dtype=object
        self.np_array: np.ndarray = np.array([copy.deepcopy(item) for item in starting_sequence] + [None] * (self.physical_size - self.logical_size), dtype=object)

        # Ensure deep copies when initializing
        for i, item in enumerate(starting_sequence):
            self.np_array[i] = copy.deepcopy(item)


    @overload
    def __getitem__(self, index: int) -> T:
        return self.np_array[index]
    
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...

    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        if isinstance(index, int):
            if index < 0 or index >= self.logical_size:
                raise IndexError("Index out of bounds")
            return self.np_array[index]
        elif isinstance(index, slice):
            start, stop, step = index.indices(self.logical_size)
            sliced_items = self.np_array[start:stop]
            return Array(sliced_items.tolist(), data_type=self.data_type)  # Return Array of the slice
        else:
            raise TypeError("Index must be an integer or slice")
    
    def __setitem__(self, index: int, item: T) -> None:
        if not isinstance(item,self.data_type):
            raise TypeError(f"Item should {self.data_type.__name__}, but got {type(item).__name__}")
        self.np_array[index]=copy.deepcopy(item)

    def __grow(self, new_size: int) -> None:
        if new_size <= self.physical_size:
            exit
        
        new_array: np.ndarray = np.array([None]* new_size, dtype= object)

        for index in range(self.logical_size):
            new_array[index] = self.np_array[index]

        self.np_array = new_array
        self.physical_size = new_size

    def append(self, data: T) -> None:
        if self.physical_size == self.logical_size:
            self.__grow(2 * self.physical_size)
        
        self.np_array[self.logical_size] = copy.deepcopy(data)
        self.logical_size += 1

    def append_front(self, data: T) -> None:
        if self.physical_size == self.logical_size:
            self.__grow(2 *self.physical_size)

        for i in range(self.logical_size, 0, -1):
            self.np_array[i] = self.np_array[i-1]

        self.np_array[0] = copy.deepcopy(data)
        self.logical_size += 1

    def pop(self) -> None:
        self.logical_size-=1
        if self.logical_size <= (1/4)*self.physical_size:
            self.physical_size = self.physical_size*(1/2)
    
    def pop_front(self) -> None:
        self.np_array = np.delete(self.np_array,0)
        self.logical_size -= 1
        if self.logical_size <= (1/4)*self.physical_size:
            self.physical_size = self.physical_size*(1/2)

    def __len__(self) -> int: 
        return self.logical_size

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Array) == False:
            return False
        if self.logical_size != other.logical_size:
            return False
        for index in range(self.logical_size):
            if self.np_array[index] !=other.np_array[index]:
                return False
        return True
    
    def __iter__(self) -> Iterator[T]:
        for i in range(self.logical_size):
            if isinstance(self.np_array[i], np.generic):
                yield self.np_array[i].item
            else:
                self.np_array[i]

    def __reversed__(self) -> Iterator[T]:
        reversed_array = self.np_array[::-1]
        return iter(self)

    def __delitem__(self, index: int) -> None:

        if index >= self.logical_size or index <0:                      
            raise IndexError ("Your inputed index is out of bounds")
        
        self.np_array = np.delete(self.np_array,index)
        self.logical_size -= 1
        
        if self.logical_size <= (1/4)*self.physical_size:
            self.physical_size = self.physical_size*(1/2)

    def __contains__(self, item: Any) -> bool:      #D
        for index in range(self.logical_size):
            if self.np_array[index] == item:
                return True
        return False
    

    def clear(self) -> None:                        #D
        self.logical_size = 0
        for index in range(self.logical_size):
            self.np_array[index]= None


    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.logical_size}, Physical: {self.physical_size}, type: {self.data_type}'
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')