
def __init__(self, n=4, m=3):
    self.n = n  # 进程数量
    self.m = m  # 资源有多少类

    self.Available = []  # 可用资源向量

    self.Max = {}  # 最大需求矩阵
    for i in range(0, self.n):
        self.Max["P{}".format(i)] = []
    self.Allocation = {}  # 分配矩阵
    for i in range(0, self.n):
        self.Allocation["P{}".format(i)] = []
    self.Need = {}  # 需求矩阵
    for i in range(0, self.n):
        self.Need["P{}".format(i)] = []
    self.Request = {}
    for i in range(0, self.n):
        self.Request["P{}".format(i)] = []

def sendRequest(self, Px, vector):
    '''
    :param Px: 字符串...P0-P4
    :param vector: 请求向量，为一个列表
    :return:
    '''
    self.checkRequestInputValid()
    self.Request[Px] = vector
    print(self.Request)
    for i in range(0, self.m):
        if self.Request[Px][i] > self.Need[Px][i]:
            raise CommonError("{}申请的资源数目Available[{}]不应该超过它的需求数目".format(Px, i))
        if self.Request[Px][i] > self.Available[i]:
            raise CommonError("{}需要等待，因为目前可用资源 Available[{}] 不够".format(Px, i))

    tmp_Available = self.Available
    tmp_Allocation = self.Allocation
    tmp_Need = self.Need

    for i in range(0, self.m):
        tmp_Available[i] = tmp_Available[i] - self.Request[Px][i]
        tmp_Allocation[Px][i] = tmp_Allocation[Px][i] + self.Request[Px][i]
        tmp_Need[Px][i] = tmp_Need[Px][i] - self.Request[Px][i]

    if self.checkTmpMatrixSafe(tmp_Available, tmp_Allocation, tmp_Need) is True:
        print("[+] Check safe ; Format changed")
        self.Allocation = tmp_Allocation
        self.Available = tmp_Available
        self.Need = tmp_Need


# 这里的查找不是很好实现。我的做法是找到一个可用的之后回退，再找一次前面的，方法比较low。可能思路有些不太对。不知道操作系统里是如何实现的

    def checkTmpMatrixSafe(self, tmp_Available, tmp_Allocation, tmp_Need):
        Work = tmp_Available
        Finish = [False] * self.n

        # finding valid i

        def helperChecker(tmp_Need_Px, Work, m):
            tag = True
            for i in range(0, m):
                if tmp_Need_Px[i] > Work[i]:
                    tag = False
            return tag

        for i in range(0, self.n):
            if Finish[i] is True:
                continue
            if Finish[i] is False and helperChecker(tmp_Need["P{}".format(i)], Work, self.m):
                print("[*] Finding P{} safe".format(i))
                for j in range(0, self.m):
                    Work[j] = Work[j] + tmp_Allocation["P{}".format(i)][j]
                Finish[i] = True
                print(Work)
                '''
                「将上述操作重复一边，范围是 (0,i) 感觉这里有可以优化的地方」
                '''
        if Finish == [True] * self.n:
            # tmp_Available = __tmp_Available
            return True
        else:
            return False