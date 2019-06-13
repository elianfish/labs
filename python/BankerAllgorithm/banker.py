#-*- coding: UTF-8 -*-


import sys
import numpy as np
import pandas as pd
import prettytable as pt
import copy


"""
进程名变量 processname          //存放进程名
可利用资源向量Available[m]      //系统中所配置该类全部可用资源数据目，随资源分配和回收而动态改变
最大需求矩阵Max[n][m]          // n个进程中每个进程对m类资源的最大需求数
分配矩阵Allocation[n][m]     // 系统中每一类资源已分配给每一进程的资源数
需求矩阵Need[n][m]            // 每一个进程尚需的各类资源数
请求向量Request[m]            //进程申请资源数据目
工作向量work[m]               //系统可提供给进程继续运行所需的各类资源数目
标记向量finish                // 用来表示系是否有足够的资源分配给进程
安全系列码向量sequence         // 用来记录安全系列码
"""

class banker():
    def __init__(self, resoures, available):
        '''
        初始化
        '''
        #self.processes = []
        self.resoures = resoures
        self.res_num = len(resoures)
        self.available = np.array(available)
        #self.max = np.array()
        self.allocation = np.array('[]')
        self.sequence = []
        self._sys_statu()

    def set_allocation(self, allo):
        return allo

    def execute(self, processes, max_data, request_data, count):
        req_processes = np.array(processes)
        pn_num = len(processes)
        max = np.array(max_data).reshape((pn_num, self.res_num))
        request = np.array(request_data).reshape((pn_num, self.res_num))
        if count == 1:
            self.allocation = np.zeros((pn_num, self.res_num), dtype=np.int64)

        #allocation = np.zeros((pn_num, self.res_num), dtype=np.int64)
        need = max - self.allocation   # 还需要多少个（最大需求-已分配数）

        print('###当前初始状态:')
        self._show_table(req_processes, max, self.allocation, need)

        for i in range(0, pn_num):
            print('=====进程{}请求资源数{}====='.format(processes[i], request[i]))
            if np.all(request[i] <= need[i]):
                if np.all(request[i] <= self.available):
                    self.available -= request[i]  # 可利用资源减少
                    need[i] -= request[i]  # 尚需的资源数减少
                    self.allocation[i] += request[i]  # 已分配资源增加:
                    self._show_table(req_processes, max, self.allocation, need)
                    if self._check_safe(processes, need, self.allocation):
                        print("系统处于安全状态")
                        print("进程{}分配的安全系列：{}".format(processes[i], self.sequence))
                    else:
                        print("系统处于不安全状态,资源分配回滚")
                        self.available += request[i]  # 可利用资源恢复
                        need[i] += request[i]  # 尚需的资源数恢复
                        self.allocation[i] -= request[i]  # 已分配资源恢复
                else:
                    print("{}请求超出可利用的资源{}，请等待".format(request[i], self.available))
                    return
            else:
                print("{}线程请求超出所需总资源数{},请等待".format(request[i], need[i]))
                return


    def _show_table(self, processes, max, allocation, need):
        resdata = '   '.join(self.resoures)
        availabledata = '  '.join(map(str, list(self.available)))

        table = pt.PrettyTable()
        table.field_names = ["Process", "Max", "Allocation", "Need", "Available"]
        table.add_row(["   ", resdata, resdata, resdata, resdata])

        for item, name in enumerate(processes):
            maxdata = '  '.join(map(str, list(max[item])))
            allocationdata = '  '.join(map(str, list(allocation[item])))
            needdata = '  '.join(map(str, list(need[item])))


            table.add_row([name, maxdata, allocationdata, needdata, availabledata])

        print(table)

    def _show(self, processes, max, request, allocation, need):
        print('***************************************')
        print('你当前请求的资源分别是：\n{}'.format(processes))
        print('进程当前请求的资源最大需求数分别是：\n{}'.format(max))
        print('进程当前请求的资源需求数是：\n{}'.format(request))
        print('进程当前已分配的资源数是：\n{}'.format(allocation))
        print('进程当前还需要的资源数是：\n{}'.format(need))
        print('***************************************')

    def _sys_statu(self):
        print("系统当前可用资源状态:")
        print ('    '.join(self.resoures))
        print ('   '.join(str(res_num) for res_num in self.available.tolist()))


    def _check_safe(self, processes, need, allocation):
        '''
        安全系列算法
        '''
        n = len(processes)
        work = copy.deepcopy(self.available)
        work_all = np.zeros((n, self.res_num), dtype=np.int64)
        finish = [False]* n
        temp_seg = []
        #while False in finish:
            #print('false in finish')
        for item, name in enumerate(processes):
            if (finish[item] == False and np.all(need[item] <= work)):
                work_all[item] = work
                work += allocation[item]
                finish[item] = True
                temp_seg.append(name)
            else:
                break

        if all(finish):
            self._show_safe_table(processes, work_all, allocation, need, finish)
            self.sequence = temp_seg
        return all(finish)

    def _show_safe_table(self, processes, work, allocation, need, finish):
        resdata = '   '.join(self.resoures)

        table = pt.PrettyTable()
        table.field_names = ["Process","work", "Allocation", "Need", "Work + Allocation", "Finish"]
        table.add_row(["   ", resdata, resdata, resdata, resdata, "  "])

        for item, name in enumerate(processes):
            workdata = '  '.join(map(str, list(work[item])))
            allocationdata = '  '.join(map(str, list(allocation[item])))
            needdata = '  '.join(map(str, list(need[item])))
            workallodata = '  '.join(map(str, list(work[item] + allocation[item])))

            table.add_row([name, workdata, allocationdata, needdata, workallodata, finish[item]])

        print(table)

def main():
    R = 5
    resources = ['A','B','C','D','E']
    available = np.full(5, 50)     # 系统资源
    bank = banker(resources, available)
    req_count = 1
    while(True):
        x = input('>>第{}次申请,请问是否为进程申请资源(Y|N)?'.format(req_count))  # 提示输入
        if x == 'N':
            print('程序结束运行')
            break
        elif x == 'Y':
            input_process = input(">>请输入进程(按逗号隔开)，例如：p0,p1,p2,p3...：")
            processlist = input_process.split(',')
            pn_num = len(processlist)
            if pn_num <= 0:
                print("提醒：进程不能为空，请重新输入")
                continue

            shape_num = pn_num * R
            input_max = input(">>请输入进程{}分别对5类资源的最大需求数(按逗号隔开) :\n".format(','.join(processlist)))
            max_data = list(map(int, input_max.split(',')))
            if len(max_data) <= 0:
                print("提醒：最大需求数不能为空，请重新输入")
                continue
            elif len(max_data) < shape_num:
                print("提醒：数据不能小于进程数{}*资资类{},请重新输入".format(pn_num, R))
                continue

            input_request = input(">>请输入进程{}分别对5类资源请求的资源数(按逗号隔开) :\n".format(','.join(processlist)))
            request_data = list(map(int, input_request.split(',')))
            if len(request_data) <= 0:
                print("提醒：资源请求数不能为空，请重新输入")
                continue
            elif len(request_data) < shape_num:
                print("提醒：资源请求数不能小于进程数{}*资资类{},请重新输入".format(pn_num, R))
                continue

            bank.execute(processlist, max_data, request_data, req_count)
            req_count += 1
        else:
            print("提醒：您的输入有误，请重新输入")
            continue

if __name__ == '__main__':
        main()
