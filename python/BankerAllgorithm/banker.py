#-*- coding: UTF-8 -*-


import sys
import numpy as np
import pandas as pd


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
        #self.allocation = np.array()
        self.sequence = []
        self._sys_statu()

    def req_resource(self, processes, processmax, processrequest):
        '''
        银行家算法
        '''

        req_processes = np.mat(processes)
        pn_num = len(processes)
        max = np.mat(processmax).reshape((pn_num, self.res_num))
        request = np.mat(processrequest).reshape((pn_num, self.res_num))
        allocation = np.zeros((pn_num, self.res_num))
        #need = np.array(max - np.sum(allocation, axis=0))
        need = max - allocation
        print(processes)
        print (max)
        print (need)

        sys.exit(0)
        for i in range(0,pn_num):
            index.append(i)

        if ((processrequest[index] <= self.Need[index]).all()):
            if ((processrequest <= self.available).all()):
                self.available -= processrequest              #可利用资源减少
                self.need[index] -= processrequest            #尚需的资源数减少
                self.allocation[index] += processrequest      #已分配资源增加
                if _check_safe(): #执行安全算法
                    print("系统处于安全状态")
                    print("进程{}分配合安全系列：".format(processname, str(self.sequence)))
                else:
                    print("系统处于不安全状态")
                    self.available += processrequest  # 可利用资源加回
                    self.need[index] += processrequest  # 尚需的资源数加回
                    self.allocation[index] -= processrequest
            else:
                print("请求超出可利用的资源，请等待")
        else:
            print("线程请求超出所需总资源数")

    def _sys_statu(self):
        print("系统当前可用资源状态:")
        print ('    '.join(self.resoures))
        print ('   '.join(str(res_num) for res_num in self.available.tolist()))


    def _check_safe(self):
        '''
        安全系列算法
        '''
        self.work = self.available
        self.finish = [False]*5
        return  True


    def _print_status(self):
        data = pd.DataFrame(index=self.processes,data=self.allocation,columns=self.resource)
        print('当前各线程使用资源如下所示：\n')
        print(data)
        data = pd.DataFrame(data=self.available.reshape(1,5),columns=self.resource)
        print('当前系统可用资源如下：\n')
        print(data)

def main():
    resources = ['A','B','C','D','E']
    available = np.full(5, 50)     # 系统资源
    print(available)
    bank = banker(resources, available)
    while(True):
        input_process = input("请输入进程，例如：p0,p1,p2,p3...：")
        processlist = input_process.split(',')
        print(processlist)
        if len(processlist) <= 0:
            print("进程不能为空，请重新输入")
            continue

        input_max = input("请输入进程{}分别对5类资源的最大需求数(按逗号隔开) :\n".format(','.join(processlist)))
        max_data = input_max.split(',')
        print(max_data)

        input_request = input("请输入进程{}分别对5类资源请求的资源数(按逗号隔开) :\n".format(','.join(processlist)))
        request_data = input_request.split(',')

        bank.req_resource(processlist, max_data, request_data)


if __name__ == '__main__':
        main()
