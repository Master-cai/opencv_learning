from pylab import *
import pandas as pd
import matplotlib.pyplot as plot


filePath = ("rain.csv")
dataFile = pd.read_csv(filePath)
summary = dataFile.describe()
print(summary)
array = dataFile.iloc[:, 1:13].values
boxplot(array)
plot.xlabel("Attribute")
plot.ylabel("Score")
show()
