from random import random # Integrated Python class
from math import e # Integrated Python class
from time import time # Integrated Python class
def A(R,T):
    A=0 # 用户体验
    Qi=[] # 每种用电器的使用率
    Ci=[] # 每种用电器的使用连贯性
    f=[] # 瞬时检测频率 len(f)==H
    U=10000 # 总用户数
    p=12 # 在电网覆盖范围内所有用电器的种类的数量
    ti=[15249.6,17654.4,2558.4,14616,18446.4,1952.16,1915.2,1940.16,5504.64,5774.4,4764.96,6609.6] # 每种用电器每天平均使用时间(s) len(ti)==p
    Pi=[2000,1200,1000,1000,1000,800,750,450,230,140,130,90] # 每种用电器功率值(每个电器由其功率值代表)
    Zi=[1,1,1,1,1,1,1,1,1,1,1,1] # 电网范围内某种电器使用率
    Vi=[1.5,1.5,1,2,2,1,1,1,1,1,1,1] # 每个用户拥有多少此类用电器
    Di=[1.96,5.93,3.47,1.68,1.62,1.7,1.3,3.56,5.73,3.95,6.74,4.51] # 每种用电器的需求评分 len(Di)==p Range:[0,10] 空调先热再冷
    Yi=[0.7,0.5,1,0.9,0.9,1,1,1,1,1,0.3,1] # 每种用电器的调节常数 len(Yi)=p Range:[0,1]
    di=[[1,1,0,0,1,0,0,0,0,0,1,0]] # 每种用电器开/关 len(di)==H len(di[i])==p 初始化di
    Ni=[] # 每种用电器每天关闭周期数 Ni<=U
    Bi=[] # 每种用电器每天关闭次数 Bi<=Ni<=U
    Kl=1 # 负荷调节效应系数
    S=50-R # 门槛频率
    ftarget=S+R*0.25 # 调节目标频率
    W=1-(1/(1+e**(-2.2*(R-2)))) # 崩溃概率
    ni=[]
    for i in range(p):
        ni.append(U*Zi[i]*Vi[i])
    Ptotal=[] # 每种用电器的总有效功率值
    for i in range(p):
        Ptotal.append(Pi[i]*ni[i])
    H=int(24*3600/T) # 每天总检测周期数
    for i in range(H):
        f.append(50-3*random())
    for i in range(H): # 针对每次调频，确定每类用电器是否关闭
        Pl=0
        di.append([])
        for j in range(p):
            di[i+1].append(1)
        for j in range(p): # 针对每种用电器计算调频前总功率
            Pl+=Ptotal[j]*di[i][j]
        deltaPj=((ftarget/50-f[i]/50)*Kl)/(1-(1-ftarget/50)*Kl)*Pl
        index=[] # 停机列表(在Pi中的序号)
        Ptotalt=Ptotal # 创建可选用电器列表，防止原始列表被改动
        for j in range(p):
            diff=[[],[]] # 寻找与减载量最相近的负荷
            for k in range(p-j): # 针对每种用电器计算与减载量的差值
                diff[0].append(Ptotalt[k]-deltaPj)
                diff[1].append(k)
            if max(diff[0])>=0:
                for l in diff[0]: # 移除功率小于减载量的负荷
                    if l<0:
                        diff[1].pop(diff[0].index(l))
                        diff[0].pop(diff[0].index(l))
                    if min(diff[0])>=0:
                           break
                index.append(diff[1][diff[0].index(min(diff[0]))]) # 将大于减载量并与减载量差值最小的用电器序号增加至停机列表
                break
            else: # 如果移除功率不足，继续移除其他功率
                index.append(diff[1][diff[0].index(max(diff[0]))])
                deltaPj-=Ptotalt[diff[0].index(min(diff[0]))] # 从减载量中去除功率最大用电器
                Ptotalt.pop(diff[0].index(max(diff[0]))) # 从可选电器列表中
        for j in index:
            di[i+1][j]=0
    for i in range(len(di[i])):
            Ni.append(0) # 初始化Ni
            Bi.append(0) # 初始化Bi
    for i in range(len(di)): # 对于每次调频
        for j in range(len(di[i])): # 对于每个用电器，计算关闭周期数/次数
            if di[i][j]==0:
                Ni[j]+=1
            if di[i][j]==0 and di[i-1][j]==1:
                Bi[j]+=1
    for i in range(p): # 计算电器使用率Qi
        if Ni[i]*T>ti[i]:
            Qi.append(0)
        else:
            Qi.append((ti[i]-Ni[i]*T)/ti[i])
    for i in range(p): # 计算连贯性Ci
        if Ni[i]==0:
            Ci.append(1)
        else:
            Ci.append((Ni[i]-(Bi[i]*Yi[i]))/Ni[i])
    for i in range(p): # 计算用户体验A
        A+=Di[i]*Yi[i]*(0.5*Qi[i]+0.5*Ci[i])*Ni[i]
    A*=W
    return A
K=0 # 门槛值
T=0 # 关闭周期时长
maxK=0
maxT=0
maxA=0
Kprecision=1
Tprecision=1
print('Please wait (Might take up to 20 minutes)')
start=time()
while Kprecision>=0.001 or Tprecision>=0.001: #计算最优解(精确到0.001)
    if A(K+Kprecision,T+Tprecision)>maxA:
        maxA=A(K+Kprecision,T+Tprecision)
        maxK=K+Kprecision
        maxT=T+Tprecision
        K+=Kprecision
        T+=Tprecision
    elif A(K+Kprecision,T+Tprecision)<=maxA and A(K,T+Tprecision)>maxA:
        maxA=A(K,T+Tprecision)
        K-=Kprecision
        if Kprecision>=0.001:
            Kprecision/=10
        maxK=K
        maxT=T+Tprecision
        K+=Kprecision
        T+=Tprecision
    elif A(K+Kprecision,T+Tprecision)<=maxA and A(K+Kprecision,T)>maxA:
        maxA=A(K+Kprecision,T)
        T-=Tprecision
        if Tprecision>=0.001:
            Tprecision/=10
        maxK=K+Kprecision
        maxT=T
        K+=Kprecision
        T+=Tprecision
    elif A(K+Kprecision,T+Tprecision)<=maxA and A(K,T)>maxA:
        maxA=A(K,T)
        K-=Kprecision
        T-=Tprecision
        if Kprecision>=0.001:
            Kprecision/=10
        if Tprecision>=0.001:
            Tprecision/=10
        maxK=K
        maxT=T
        K+=Kprecision
        T+=Tprecision
    if Kprecision<=0.0001 and Tprecision<=0.0001:
    	break
print('K={0},T={1}'.format(round(maxK+Kprecision,3),round(maxT+Tprecision,3)))
end=time()
print('Time elapsed: {0}s'.format(end-start))
