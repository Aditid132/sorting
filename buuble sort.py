# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 12:44:29 2021

@author: aditi
"""

def bubble(a):
     n=len(a)
     
     for i in range(n):
         for j in range(0,n-i-1):
             if(a[j]>a[j+1]):
                 tmp=a[j]
                 a[j]=a[j+1]
                 a[j+1]=tmp
                 
    
    
                
                
a=[5,1,4,2,8]
bubble(a)

for i in  a:
    print(i)
        