import copy
from typing import Callable, Iterator, Optional, Tuple
from datastructures.ihashmap import KT, VT, IHashMap
from datastructures.array import Array
import pickle
import hashlib

from datastructures.linkedlist import LinkedList

class HashMap(IHashMap[KT, VT]):

    def __init__(self, number_of_buckets=7, load_factor=0.75, custom_hash_function: Optional[Callable[[KT], int]]=None) -> None:

        self._buckets : Array[LinkedList[Tuple[KT,VT]]] = \
            Array(starting_sequence =[LinkedList(data_type=tuple) for _ in range(number_of_buckets)], 
                  data_type=LinkedList)
        
        self._count : int = 0
        self._load_factor_threshold : float = load_factor
        self._hash_function = custom_hash_function or self._default_hash_function

    def _get_bucket_number (self, key: KT):
        return self._hash_function(key) % len(self._buckets)
    
    def __getitem__(self, key: KT) -> VT:
        # 1 comp bucket based on key
        bucket_index : int = self._get_bucket_number(key)
        # 2 get bucket chains in that bucket 
        bucket_chain = self._buckets[bucket_index]
        # 3 is there a tuple with this key in it 
        for (k, v) in bucket_chain:         #can make a two variable item
            if k == key:
                return v
        raise KeyError("no key was found")
    
    @staticmethod
    def _is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    @staticmethod
    def _next_prime_after_double(n: int) -> int:
        next_prime = n * 2
        while not HashMap._is_prime(next_prime):
            next_prime += 1
        return next_prime
    


    def __setitem__(self, key: KT, value: VT) -> None:
        if not isinstance(value, str):
            raise TypeError("The value must be a string.")

        bucket_index = self._get_bucket_number(key)
        bucket_chain = self._buckets[bucket_index]

        for idx, (k, v) in enumerate(bucket_chain):
            if k == key:
                bucket_chain[idx] = (key, value)
                break
        else:
            bucket_chain.append((key, value))
            self._count += 1
        if (self._count / len(self._buckets)) > self._load_factor_threshold:
            self._resize()

    def _resize(self) -> None:
        old_buckets = self._buckets
        new_size = self._next_prime_after_double(len(old_buckets))

        self._buckets = Array(starting_sequence=[LinkedList(data_type=tuple) for _ in range(new_size)],
                              data_type=LinkedList)
        old_count = self._count
        self._count = 0
        for bucket in old_buckets:
            for (k, v) in bucket:
                self[k] = v 

        self._count = old_count




    def keys(self) -> Iterator[KT]:
        for i in self._buckets:
            for (k,v) in i:
                yield k
    
    def values(self) -> Iterator[VT]:
        for i in self._buckets:
            for (k,v) in i:
                yield v


    def items(self) -> Iterator[Tuple[KT, VT]]:
        for i in self._buckets:
            for (k, v) in i:
                yield (k, v) 
            
    def __delitem__(self, key: KT) -> None:
        bucket_index = self._get_bucket_number(key)
        bucket_chain = self._buckets[bucket_index]

        for idx, (k, v) in enumerate(bucket_chain):
            if k == key:
                del bucket_chain[idx]
                self._count -= 1
                break
        else:
            raise KeyError(f"Key {key} not found for deletion.")

    

    
    def __contains__(self, key: KT) -> bool:
        # 1 comp bucket based on key
        bucket_index : int = self._get_bucket_number (key)
        # 2 get bucket chains in that bucket 
        bucket_chain : LinkedList[tuple] = self._buckets[bucket_index]
        # 3 is there a tuple with this key in it 
        for (k, v) in bucket_chain:         #can make a two variable item
            if k == key:
                return True                                                                  
        return False
    
    def __len__(self) -> int:
        return self._count
    
    def __iter__(self) -> Iterator[KT]:
        return self.keys()
    
    def __eq__(self, other: object) -> bool:
        raise NotImplementedError("HashMap.__eq__() is not implemented yet.")

    def __str__(self) -> str:
        return "{" + ", ".join(f"{k}: {v}" for (k, v) in self.items()) + "}"
    
    def __repr__(self) -> str:
        return f"HashMap({str(self)})"

    @staticmethod
    def _default_hash_function(key: KT) -> int:
        """
        Default hash function for the HashMap.
        Uses Pickle to serialize the key and then hashes it using SHA-256. 
        Uses pickle for serialization (to capture full object structure).
        Falls back to repr() if the object is not pickleable (e.g., open file handles, certain C extensions).
        Returns a consistent integer hash.
        Warning: This method is not suitable
        for keys that are not hashable or have mutable state.

        Args:
            key (KT): The key to hash.
        Returns:
            int: The hash value of the key.
        """
        try:
            key_bytes = pickle.dumps(key)
        except Exception:
            key_bytes = repr(key).encode()
        return int(hashlib.md5(key_bytes).hexdigest(), 16)