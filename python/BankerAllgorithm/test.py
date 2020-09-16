import numpy as np
import pandas as pd
import prettytable as pt


#矩阵初始化0
allocation = np.zeros((2))
print(allocation)

#列表转矩阵
input_data="13,29,32,14,15,26,7,8,9,10"
mat_data=np.mat(input_data).reshape((2,5))
print(mat_data)

#输出列表元素值
list_data=['11', '13', '15', '16', '17', '12', '15', '15', '16', '16']
print(len(list_data))
mat_data=np.mat(list_data).reshape((2,5))
print(mat_data)
print (mat_data[0,1])
print (mat_data[1,2])

# 矩阵比较
allocation = np.zeros((1,5))
print(allocation)
print (np.all(allocation)) #false

allocation = np.ones((1,5)) #True
print(allocation)
print (np.all(allocation))

request = ['3','4','5']
need = ['2','1','4']
need1 = ['5','6','7']
print(np.all(request > need)) #True
print(np.all(request > need1)) #false


#初始值

allocation = np.zeros((2,5), dtype=np.int64)
print(allocation.dtype)
#allocation = np.arange(0,0).reshape((2, 5))
input_request = '1,2,15,6,4,3,7,8,9,10'
request_data = list(map(int, input_request.split(',')))
request = np.array(request_data).reshape((2, 5))
print (request[0])
print(allocation[0])
allocation[0] += request[0]
print(allocation)

#    
available = np.full(6, 50).reshape((1,6))
print(available)
print(available.dtype)

#数组维护变更
print("#数组维度变更")
allo_list = []
allocation = np.array(allo_list)
allocation = np.zeros((2, 5), dtype=np.int64)
print(allocation)


#列表
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)
a = ['P0', 'P1', 'P2']
b = ['P0', 'P1', 'P2']
c = print(sorted(list(set(a+b))))
print(c)
a = ['P0', 'P1', 'P2']
b = ['P0']
c = print(sorted(list(set(a+b))))
print(c)

#表格测试
resources = ['A', 'B', 'C', 'D', 'E']
print (('  ').join(resources))
available = np.full(10, 50).reshape((2, 5))  # 系统资源
max = np.full(10, 30).reshape((2, 5))  # 系统资源
allocation = np.zeros((2, 5), dtype=np.int64)
Need = np.full(10, 30).reshape((2, 5))  # 系统资源
print(available)
print('  '.join(map(str, list(max[0]))))
print(('  ').join(map(str, available)))

def show_table():
    process = ['p0','p1']
    resdata = '   '.join(resources)

    table = pt.PrettyTable()
    table.field_names = ["resoure", "Max", "Allocation", "Need", "Available"]
    table.add_row(["   ", resdata, resdata, resdata, resdata])

    for item, name in enumerate(process):
        print (item, name)
        maxdata = '  '.join(map(str, list(max[item])))
        allocationdata = '  '.join(map(str, list(allocation[item])))
        needdata = '  '.join(map(str, list(Need[item])))
        availabledata = '  '.join(map(str, list(available[item])))

        table.add_row([name, maxdata, allocationdata, needdata, availabledata])

    print(table)

show_table()