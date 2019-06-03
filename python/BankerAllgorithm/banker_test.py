#-*- coding: UTF-8 -*-


import numpy as np                                                                      #导入numpy模块

#初始化各数据结构
Available = np.array([3,3,2])                                             #可利用各资源总数
Max = np.array([[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]])                 #各进程最大需求资源数
Allocation = np.array([[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]])          #已分配各进程的资源数
Need = np.array([[7,4,3],[1,2,2],[6,0,0],[0,1,1],[4,3,1]])                #各进程尚需的资源数
safeList=[]                                                               #安全进程执行序列
Request=[]                                                                #各进程对各资源的请求
Request_name=""                                                           #进程名称


def input_Request():
    global Allocation,Available,Max,Need,safeList,Request,Request_name
    try:
        Request_name=input("请输入请求线程的编号：\n0   1    2    3    4\n")
        Request_name=int(Request_name)
        Request_new=input("请输入P{}的请求资源数(如：* * *) :\n".format(Request_name))
        Request_new=list(Request_new)

        print (Request_new)
        for x in range(0,5,2):                                                          #去除输入的空格
            i=int(Request_new[x])
            Request.append(i)

        Request=np.array(Request)
    except:
        print("输入错误，请重新输入")
        input_Request()


def BankerAlgorithm():
    global Allocation,Available,Max,Need,safeList,Request,Request_name
    input_Request()

    if ((Request<=Need[Request_name]).all()):
        if ((Request<=Available).all()):
            Available -=Request                                                          #可利用资源减少

            Need[Request_name] -= Request                                                #尚需的资源数减少
            Allocation[Request_name] +=Request                                           #已分配资源增加
            safeAlgorithm()                                                              #执行安全算法
        else:
            print("请求超出可利用的资源，请等待")
            return
    else:
        print("线程请求超出所需总资源数")
        return

def safeAlgorithm():
    work = Available                                                                      #分配work向量
    Finish=[False]*5                                                                    #分配Finish向量

    while False in Finish:
        for i in range(0,5):
           for j in range(0,3):
                if ((Finish[i]==False) and ((Need[i]<=work).all())):
                    for m in range(3):
                        work[m] =work[m]+ Allocation[i][m]
                    Finish[i]=True
                    safeList.append(i)
                else:
                    break

    if False in Finish:
        print("*"*45)
        print("您输入的请求资源数:{}".format(Request))
        print("您输入的请求进程是{}".format(Request_name))
        print("系统安全性：不安全状态")
        print("*"*45)
    else:
        print("*"*45)
        print("您输入的请求进程是{}".format(Request_name))
        print("您输入的请求资源数:{}".format(Request))
        print("系统安全性：系统安全")
        print("安全序列为：",safeList)
        print("*"*45)



if __name__ =="__main__":

    BankerAlgorithm()