#h will be calculated by the given formula. Using a "n" to finish the loop and the calculation.
h = 0
for n in range(1,6):
    #use range to make "n"s an arithmetic sequence
    h = n*(2*n-1)
    print(n,int(h))