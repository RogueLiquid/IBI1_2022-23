import os
import re
print(os.getcwd())
file1 = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa","r")
file2 = open("TGA_genes.fa","w")
sq = ""
gn = []
for line in file1:
    if line.startswith(">"):
        if gn and sq.endswith("TGA"):
                file2.write(">" + gn[0] + "\n" + sq + "\n")
        gn = re.findall(">(\w+)",line)
        sq = ""
    else:
        line = line.strip()
        sq += line
        
if gn and sq.endswith("TGA"):
    file2.write(">" + gn[0] + "\n" + sq + "\n")
file1.close()
file2.close()
