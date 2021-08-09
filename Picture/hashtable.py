#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 16:10:58 2021

@author: jenny
"""
set(nums1).intersection(set(nums2))
    for key,i in hashmap.items():
        if i>1:
            del hashmap[key]
            
            
        hashmap = {}
        for i,num in enumerate(s):
            if num not in hashmap:
                hashmap[num]= 1
            else:
                hashmap[num] = hashmap.get(num)+1
        le = []
        for key,i in hashmap.items():
            if i>1:
                le.append(key)
        for i in le:
            for key in list(hashmap.keys()):
                if i== key:
                    del hashmap[key]
            
        if hashmap:
            x.keys().index("d")
            print(s.index(list(hashmap.keys())[0]))
        else:
            print(-1)
            
            
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

for key in hashmap.keys():
    for val in hashmap[key]:
        if val not in 
        
