# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 14:36:13 2023

@author: xyh
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("D:/college/first year/IBI1/practical/")

#question1
covid_data = pd.read_csv("full_data.csv")
print (covid_data)

#question2
print(covid_data.iloc[0:1000:100,1])

#question3
location = covid_data.loc[:,"location"]
locationrows = location == "Afghanistan"
print(covid_data.loc[locationrows, "total_cases"])

#question4
date = covid_data.loc[:,"date"]
daterows = date == "2020-03-31"
print("the new cases is",covid_data.loc[daterows, "new_cases"].mean(0))
print("the new deaths is",covid_data.loc[daterows, "new_deaths"].mean(0))

#question5
dateboxplot = covid_data.loc[daterows, ["new_cases","new_deaths"]]
plt.boxplot(dateboxplot)
plt.show()

#question6
date6 = covid_data.loc[location == "World", "date"]
newcases = covid_data.loc[location == "World",["new_cases", "new_deaths"]]
plt.plot(date6, newcases)
plt.xticks(date6.iloc[0:len(date6):4],rotation=-90)
plt.title("New Cases and New Deaths of World")
plt.show()