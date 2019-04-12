from pylab import *
import pandas as pd
import matplotlib.pyplot as plot


filePath = ("rain.csv")
dataFile = pd.read_csv(filePath)
summary = dataFile.describe()
minRing = -1
maxRing = 99
nrows = 11
for i in range(nrows):
    dataRow = dataFile.iloc[i, 1:13]
    labelColor = (dataFile.iloc[i, 12] - minRing) / (maxRing - minRing)
    dataRow.plot(color=plot.cm.RdYlBu(labelColor), alpha=0.5)
plot.xlabel("Attribute")
plot.ylabel("Score")
show()
