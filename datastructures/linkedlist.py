from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Optional, Sequence, Iterator
from datastructures.ilinkedlist import ILinkedList, T


class LinkedList[T](ILinkedList[T]):

    @dataclass
    class Node:
        data: T
        next: Optional[LinkedList.Node] = None
        previous: Optional[LinkedList.Node] = None

    def __init__(self, data_type: type = object) -> None:
        self.count = 0 
        self.head: Optional[LinkedList.Node] = None      #opt used to say it can be none or node data type
        self.tail: Optional[LinkedList.Node] = None
        self.data_type = data_type

    @staticmethod
    def from_sequence(sequence: Sequence[T], data_type: type=object) -> LinkedList[T]:
        llist = LinkedList(data_type=data_type)   #static method so it doesnt reference self 
        for item in sequence:
            if not isinstance(item,data_type):
                raise TypeError ("Wrong data type")
            llist.append(item)
        return llist

    def append(self, item: T) -> None:
        if not isinstance(item,self.data_type):
            raise TypeError ("Wrong data type")
        node = LinkedList.Node(data = item)

        if self.empty:
            self.head = self.tail = node
        else:     #if not self.empty:
		#set nodes previous to current tail
            node.previous = self.tail
		#set tail next to new node
            if self.tail:
                self.tail.next = node 	
		#set tail to new node 
            self.tail = node
        self.count+=1


    def prepend(self, item: T) -> None:
        new_node = LinkedList.Node (data = item)

        if not isinstance(item,self.data_type):
            raise TypeError ("Wrong data type")
        new_node.next = self.head 
        if self.head:
            self.head.previous = new_node
        self.head = new_node
        self.count += 1

    def insert_before(self, target: T, item: T) -> None:
        travel = self.head 
        while travel:
            if travel.data == target:
                break 
            travel = travel.next
        if not isinstance(target, self.data_type):
            raise TypeError("Wrong data type for target")        
        if not isinstance(item,self.data_type):
            raise TypeError ("Wrong data type")
        if travel is None:
            raise ValueError(f"the target was not found")
        

        if travel is self.head:
            self.prepend(item)
            return 
        
        new_node = LinkedList.Node(data=item)
        new_node.previous = travel.previous 
        new_node.next = travel
        travel.previous.next = new_node
        travel.previous = new_node 

        self.count += 1

    def insert_after(self, target: T, item: T) -> None:
        if not isinstance(target, self.data_type):
            raise TypeError("Wrong data type for target")            
        if not isinstance(item,self.data_type):
            raise TypeError ("Wrong data type")         
        travel = self.head 
        while travel:
            if travel.data == target:
                break 
            travel = travel.next

        if travel is None:
            raise ValueError(f"the target was not found")
       
        if travel is self.tail:
            self.append(item)
            return 
        
        new_node = LinkedList.Node(data=item)
        new_node.next=travel.next
        new_node.previous= travel
        travel.next.previous=new_node
        travel.next=new_node

        self.count += 1

    def remove(self, item: T) -> None:
        if not isinstance(item,self.data_type):
            raise TypeError ("Wrong data type")        
        travel = self.head 
        
        while travel:
            if travel.data == item:
                break 
            travel = travel.next

        if travel is None:
            raise ValueError("does not exist")
        else:
            if travel == self.head:
                self.head = travel.next
                if self.head:
                    self.head.previous = None 

            elif travel == self.tail:
                self.tail = travel.previous
                if self.tail:
                    self.tail.next = None 

            else:
                travel.next.previous = travel.previous
                travel.previous.next = travel.next

            travel.next = travel.previous = None 
            self.count -= 1
        

    def remove_all(self, item: T) -> None:
        travel = self.head
        if not isinstance(item,self.data_type):
            raise TypeError ("Wrong data type")
        while travel:
            if travel.data == item:
                if travel == self.head:
                    self.head = travel.next
                    if self.head:
                        self.head.previous = None
                elif travel == self.tail:
                    self.tail = travel.previous
                    if self.tail:
                        self.tail.next = None
                else:
                    travel.previous.next = travel.next
                    if travel.next:
                        travel.next.previous = travel.previous
                next_node = travel.next  
                travel.next = travel.previous = None
                self.count -= 1
                travel = next_node
            else:
                travel = travel.next

    def pop(self) -> T:
        if self.tail is None:
            raise IndexError("Out of Index")
        else:
            data = self.tail.data
            if self.head != self.tail:
                self.tail = self.tail.previous
                self.tail.next = None
                self.count -= 1
                return data
            self.head=self.tail=None



    def pop_front(self) -> T:
        if self.head is None:
            raise IndexError("Out of Index")
        else:
            data = self.head.data
            if self.head != self.tail:
                self.head = self.head.next
                self.head.previous = None
                self.count -= 1
                return data
            self.head=self.tail=None       

    @property
    def front(self) -> T:
        if self.empty:
            raise IndexError("List is empty")
        return self.head.data

    @property
    def back(self) -> T:
       if self.empty:
           raise IndexError("List is empty")
       return self.tail.data

    @property
    def empty(self) -> bool:
        return self.head is None

    def __len__(self) -> int:
        return self.count 
    
    def clear(self) -> None:
        self.count = 0
        self.head=self.tail=None

    def __contains__(self, item: T) -> bool:
        current = self.head
        while current is not None:
            if current.data == item:
                return True       
            current = current.next

        return False

    def __iter__(self) -> Iterator[T]:
        self._travel_node = self.head
        return self

    def __next__(self) -> T:
        travel = self._travel_node
        
        if travel is None:
            raise StopIteration
        
        
        data = travel.data  
        
        
        self._travel_node = travel.next
        
        return data
    
    def __reversed__(self) -> LinkedList[T]:
        #yielding approach but start at tail
        travel=self.tail
        while travel:
            yield travel.data

            travel=travel.previous 
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LinkedList):
            return False

        if self.count != other.count:
            return False 
        

        travel = self.head 
        current = other.head 

        while travel is not None and current is not None:
            if travel.data != current.data:
                 return False
            else:
                travel = travel.next 
                current = current.next  
        return True 


    def __str__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"LinkedList({' <-> '.join(items)}) Count: {self.count}"


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
