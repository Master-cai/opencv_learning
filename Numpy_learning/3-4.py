import numpy as np
import pylab
import scipy.stats as stats


data = np.mat([[1, 200, 105, 3, False],
              [2, 165, 80, 2, False],
              [3, 184.5, 120, 2, False],
              [4, 116, 70.8, 1, False],
              [5, 270, 150, 4, True]]
              )

coll = []
for row in data:
    coll.append(row[0, 1])

stats.probplot(coll, plot=pylab)
pylab.show()
