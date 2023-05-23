# -*- coding: utf-8 -*-
"""
Created on Tue May 23 11:07:08 2023

@author: xyh
"""

import os
import re
print(os.getcwd())
file1 = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa","r")
file2 = open("TGA_stop_genes.fa","w")

count = 0
sq = ""
gn = []
for line in file1:
    if line.startswith(">"):
        if gn and sq.endswith("TGA"):
                file2.write(">" + gn[0] + "\n" + sq + "\n")
                count +=1
        gn = re.findall(">(\w+)",line)
        sq = ""
    else:
        line = line.strip()
        sq += line
        

if gn and sq.endswith("TGA"):
    file2.write(">" + gn[0] + "\n" + sq + "\n")
    count +=1
file2.write("the total gene number is " + str(count))
file1.close()
file2.close()
