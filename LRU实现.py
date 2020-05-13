# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 00:36:58 2020

@author: 11597
"""

from collections import OrderedDict

def prn_obj(obj):
    print('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]) )
  
class LRUCache(OrderedDict):
    def __init__(self, capacity):
        self.capacity = capacity
    
    def get(self, key):
        if key not in self:
            return -1
        
        self.move_to_end(key)
        return self[key]
    
    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
            self[key]=value
        
        if len(self)>self.capacity:
            self.popitem(last=False)
            
            
obj = LRUCache(5)

obj.put('a', 1)
obj.put('b', 2)
obj.put('c', 3)

print(obj.get('a'))

print(dir(obj))
        