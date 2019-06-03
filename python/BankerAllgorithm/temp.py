#-*- coding: UTF-8 -*-

import numpy as np
import copy
import itertools
import pandas as pd


class Bank:
    def __init__(self, need, allocation):
        self.threads = ['p0', 'p1', 'p2', 'p3', 'p4']
        self.resource = ['A', 'B', 'C', 'D', 'E']
        self.indexs = [0, 1, 2, 3, 4]
        self.finish = [False for i in range(5)]
        self.safeList = []
        self.safeListitem = ['-' for i in range(5)]
        self.allocation = np.array(allocation)
        self.max = np.full(5, 50)
        self.need = np.array(need)
        self.available = np.array(self.max - np.sum(self.allocation, axis=0))
        # self.printResource()
        self.isSafe(self.indexs[:], self.available)
        if len(self.safeList) > 0:
            print('T0时刻系统处于安全状态，安全序列：{}'.format(self.safeList[0]))
        else:
            print("T0时刻没有安全序列！")
            self.reSume()
            self.printTable()

    def reSume(self):
        self.finish = np.full(5, False)
        self.safeList = []
        self.safeListitem = ['-' for i in range(5)]

    def printTable(self):
        data = pd.DataFrame(index=self.threads,data=self.allocation,columns=self.resource)
        print('当前各线程使用资源如下所示：\n')
        print(data)
        data = pd.DataFrame(data=self.available.reshape(1,5),columns=self.resource)
        print('当前系统可用资源如下：\n')
        print(data)



    def request(self, threaName, needed):

        index = self.threads.index(threaName)  # 根据进程名称获取进行在列表中索引值
        needed = list(map(lambda x: int(x), needed))  # 将输入的字符串转为int类型

        if np.all(needed > self.need[index]):
            print('{}线程申请的资源{}无效,超过所需资源数'.format(threaName, needed))
            return
        if np.all(needed > self.available):
            print('{}线程申请的资源{}无效,超过剩余可用资源'.format(threaName, needed))
            return


        #对资源进行变更
        self.need[index] -= needed
        self.allocation[index] += needed
        self.available -= needed
        self.isSafe(self.indexs[:], self.available)
        if len(self.safeList) > 0:
            print(self.safeList[0])
            self.printTable()
        else:
            #如果不存在安全序列，回退已经变更的资源
            self.need[index] += needed
            self.allocation[index] -= needed
            self.available += needed
            print('{}线程申请的资源{}无效,不存在安全序列'.format(threaName, needed))
        self.reSume()

    def isSafe(self, series, works, n=0):
        print(works)
        if series == None:
            return np.all(self.finish)
        for j, i in enumerate(series):

            if np.all(works >= self.need[i]) == False: #判断剩余资源是满足当前线程所需数量
                continue
            else:#资源满足当前线程所需时，执行下面的代码
                self.finish[i] = True#设置为True，表是当前线程满足条件
                self.safeListitem[n] = self.threads[i]

                seriesTemp = series[:] #深度copy
                seriesTemp.remove(i) # 删除元素i

                flg = self.isSafe(seriesTemp, works + self.allocation[i], n + 1) #递归
                if flg:#当finish列表的所有元素都为True时，将该安全队列加入safeList列表中
                    self.safeList.append(self.safeListitem[:])

                self.safeListitem[n] = '-'#初始化安全列队中第n个位置的线程为'-'
                self.finish[i] = False #初始化第i个位置的线程的状态

        return np.all(self.finish)


def main():
    #初始需求矩阵
    need = [[30, 5, 4, 5, 7],
            [40, 4, 30, 7, 4],
            [40, 7, 6, 8, 6],
            [30, 9, 8, 20, 2],
            [2, 6, 5, 4, 5]]
    #初始线程资源占用矩阵
    allocation = [[4, 5, 6, 3, 5],
                  [5, 8, 3, 5, 3],
                  [4, 6, 3, 6, 4],
                  [5, 2, 8, 7, 8],
                  [3, 5, 7, 8, 4]]
    bank = Bank(need, allocation)
    while (True):
        treadName = input("输入线程名称,可选线程包括p0,p1,p2,p3,p4：").strip()
        if bank.threads.count(treadName) == 0:
            print('输入线程名称错误，请重新输入!')
            continue
        resource = input('输入该线程对每类资源的最大需求数量，用空格隔开：').strip().split(' ')

        bank.request(treadName, resource)


if __name__ == '__main__':
    main()
