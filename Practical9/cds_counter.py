#match the pieces with the goal, then count the times the goal appears

import re
seq = "ATGCAATCGACTACGATCTGAGAGGGCCTAA"
count = 0
ans = re.findall("TAA|TAG|TGA", seq)
print(ans)
for i in ans:
    if i == "TAA" or i == "TAG" or i == "TGA" :
        count +=1
print(count)
