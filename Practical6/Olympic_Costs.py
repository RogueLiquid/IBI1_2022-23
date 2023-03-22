#sorting the following numbers
costs=[1,8,15,7,5,14,43,40]
costs.sort()
print(costs)

#I looked up for information on https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_colors.html#sphx-glr-gallery-lines-bars-and-markers-bar-colors-py to learn how to make a barplot
#I didn't want to manually sort the city so I tried to make a dictionary to match the costs and city names
import matplotlib.pyplot as plt
Dictionary = {1: "Los Angeles", 8: "Seoul", 15: "Barcelona", 7: "Atlanta", 5: "Sydney", 14: "Athens", 43: "Beijing", 40: "London"}
nation = []
for i in costs:
    nation.append(Dictionary[i])
counts = [40, 100, 30, 55]
bar_colors = ['tab:red', 'tab:blue', 'tab:orange']
plt.figure(figsize = (16,5))
plt.bar(nation, costs, width=0.8, color=bar_colors)
plt.ylabel("Money spent(in $ billions)")
plt.title("Money spend on Olympics in each city")
plt.show()
#I tried to add year in the x-axis but that would be too long, so I deleted the year.
