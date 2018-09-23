# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 19:53:41 2018

@author: Luis
"""

#For csv files where edges are separated by comma per cell.

# permutations of given length 
from itertools import combinations 
import csv
edges_dict = {}

with open('edges_to_treat.csv', 'r', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        edges_dict[row[0]] = row[1]
            
   
with open('edges.csv', 'w', encoding='utf-8', newline='') as csvfile:
    for key in edges_dict.keys():
        perm = combinations(edges_dict[key].split(','), 2)
        for i in perm:
            spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([i[0], i[1]])
