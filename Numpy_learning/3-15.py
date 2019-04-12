from pylab import *
import matplotlib.pyplot as plot
import pandas as pd


filePath = ("rain.csv")
dataFile = pd.read_csv(filePath)
summary = dataFile.describe()
corMat = pd.DataFrame(dataFile.iloc[1:20, 1:20].corr())
plot.pcolor(corMat)
plot.show()
