# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 12:19:03 2024

@author: Acer
"""

points = [(2,3),(4,5),(8,12),(11,23),(4,5)]
distances = list()


def euclideanDistance(p1,p2):
    difference_X = p2[0] - p1[0]
    difference_Y = p2[1] - p1[1]
    return ((difference_X**2)  + (difference_Y **2))**(1/2)



for i in range(len(points)):
    " i+1 "
    for j in range(i+1 , len(points)):
        if(i != j):
            print(points[i], "--",points[j])
            distances.append(euclideanDistance(points[i],points[j]))

print("min distance : ", min(distances))
print("------distances------")
print(distances)