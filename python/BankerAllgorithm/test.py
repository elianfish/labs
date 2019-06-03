import numpy as np
import pandas as pd


#矩阵初始化0
allocation = np.zeros((2))
print(allocation)

input_data="13,29,32,14,15,26,7,8,9,10"

#列表转矩阵
mat_data=np.mat(input_data).reshape((2,5))
print(mat_data)

list_data=['11', '13', '15', '16', '17', '12', '15', '15', '16', '16']

print(len(list_data))
mat_data=np.mat(list_data).reshape((2,5))
print(mat_data)


allocation = np.zeros((2,5))
print(allocation)
