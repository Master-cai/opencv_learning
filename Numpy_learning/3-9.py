from pylab import *
import pandas as pd
import matplotlib.pyplot as plot


filePath = ("dataTest.csv")
dataFile = pd.read_csv(filePath, header=None, prefix="V")
print(dataFile.head())
print((dataFile.tail()))

sumary = dataFile.describe()
print(sumary)
array = dataFile.iloc[:, 10:16].values
boxplot(array)
plot.xlabel("Attritube")
plot.ylabel("Score")
show()
