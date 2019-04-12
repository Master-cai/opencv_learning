import numpy as np
data = np.mat([[1, 200, 105, 3, False],
              [2, 165, 80, 2, False],
              [3, 184.5, 120, 2, False],
              [4, 116, 70.8, 1, False],
              [5, 270, 150, 4, True]]
              )
#row = 0
#for line in data:
#    row += 1
#    print(row)
#    print(line)
#print(data.size)
#print(data[0, 3])
#print(data[0, 4])
#print(data)
coll = []
for row in data:
#    print(row[0])
    coll.append(row[0, 1])
print(np.sum(coll))#求和
print(np.mean(coll))#均值
print(np.std(coll))#标准差
print(np.var(coll))#方差

