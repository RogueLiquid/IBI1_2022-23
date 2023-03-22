#First i will make a dictionary of movie genres and student numbers, then use "for" function to creat 2 lists to make pie chart
#I learnt how to make pie chart from https://matplotlib.org/stable/plot_types/stats/pie.html#sphx-glr-plot-types-stats-pie-py
import matplotlib.pyplot as plt
Type = ["Comedy","Action","Romance","Fantasy","Science-fiction","Horror","Crime","Documentary","History","war"]
Number = [73,42,38,28,22,19,18,12,8,7]
Dictionary = {}
count = 0
for count in range(0,len(Type)):
    Dictionary[Type[count]] = Number[count]
print(Dictionary)
plt.pie(Number, labels = Type)