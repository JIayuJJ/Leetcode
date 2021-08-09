#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 14:51:36 2021

@author: jenny
"""
nums =  [0,2,1,5,3,4]
ans = []
for i, num in enumerate(nums):
    print(num)
    print(i)
    ans.append(nums[nums[i]])
    
candidates = [0]
for x in nums:
    candidates += [x^y for y in candidates]  
    print(candidates)
return sum(candidates)

class MyHashSet:
 
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1000
        self.itemsPerBucket = 1001
        self.table = [[] for _ in range(self.buckets)]
 
    def hash(self, key):
        return key % self.buckets
 
    def pos(self, key):
        return key // self.buckets
 
    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        hashkey = self.hash(key)
        if not self.table[hashkey]:
            self.table[hashkey] = [0] * self.itemsPerBucket
        self.table[hashkey][self.pos(key)] = 1
 
    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        hashkey = self.hash(key)
        if self.table[hashkey]:
            self.table[hashkey][self.pos(key)] = 0
 
    def contains(self, key):
        """
        Returns true if this set did not already contain the specified element
        :type key: int
        :rtype: bool
        """
        hashkey = self.hash(key)
        return (self.table[hashkey] != []) and (self.table[hashkey][self.pos(key)] == 1)
