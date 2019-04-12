from pylab import *
import pandas as pd
import matplotlib.pyplot as plot


filePath = ("dataTest.csv")
dataFile = pd.read_csv(filePath, header=None, prefix="V")
summary = dataFile.describe()
corMat = pd.DataFrame(dataFile.iloc[1:20, 1:20].corr())
plot.pcolor(corMat)
plot.show()
