#x for the number of rabbits, every time x is doubled(breed), the count of generations will add 1, stop the loop when x exceed 100
x = 2
#x is the number of rabbit
count = 1
#count is the number of generation
while x <= 100:
     x = 2*x
     count +=1
print("the genereation is ",count)