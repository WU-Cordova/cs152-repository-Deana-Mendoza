from typing import Iterable, Optional
from datastructures.ibag import IBag, T


class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        self.contents = {}
        for item in items:
            if item == None:
                raise TypeError("added none item")
            elif item not in self.contents:
                self.contents[item]=1 
            else:
                self.contents[item] += 1

    def add(self, item: T) -> None:
        if item == None:
            raise TypeError("added None Item")
        elif item not in self.contents:
            self.contents[item]= 1 
        else:
            self.contents[item] += 1


    def remove(self, item: T) -> None:
        if item not in self.contents or item== None:
            raise ValueError("item not in bag")
        if item in self.contents:
            self.contents[item] -=1
        if self.contents[item] == 0:
            del self.contents[item]

        

    def count(self, item: T) -> int:
        try:
            return(self.contents[item])
        except: 
            if item == None:
                raise TypeError("counted none item")
            if item not in self.contents:
                return 0

    def __len__(self) -> int:
        total=0
        for item in self.contents:
            total+= self.contents[item]
        return total

    def distinct_items(self) -> int:
        return list(self.contents.keys())

    def __contains__(self, item) -> bool:
        if item in self.contents:
            return True 
        else: 
            return False 

    def clear(self) -> None:
        self.contents={}


    