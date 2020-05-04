from time import time # Integrated Python class
from random import random # Integrated Python class
K=1.335 # 门槛值
T=1.197 # 关闭周期时长
f0=47 # 频率响应时的初始频率值
df0=50-f0 # 频率响应时的最大频率偏差
v=0.5 # 频率响应时频率稳定上升的速度
S=50-K # 门槛频率
ftarget=S+K*0.25 # 调节目标频率
df=df0-(50-ftarget)
m=int((ftarget-f0)*T/v)+1 # 频率响应所占用的周期数
f1=f0+v*T*m # 频率响应后的首次检测频率值
df1=50-f1 # 频率响应后的最大频率偏差
tacc=T*m # 超过门槛值的频率偏差的累积时间
#print([m,tacc])
G=(df*T)/(tacc*df1)
print(G)
"""
maxK=0
maxT=0
maxG=0
Kprecision=1
Tprecision=1
print('Please wait (Might take up to 20 minutes)')
start=time()
while Kprecision>=0.001 or Tprecision>=0.001: #计算最优解(精确到0.001)
    if G(K+Kprecision,T+Tprecision)>maxG:
        maxG=G(K+Kprecision,T+Tprecision)
        maxK=K+Kprecision
        maxT=T+Tprecision
        K+=Kprecision
        T+=Tprecision
    elif G(K+Kprecision,T+Tprecision)<=maxG and G(K,T+Tprecision)>maxG:
        maxG=G(K,T+Tprecision)
        K-=Kprecision
        if Kprecision>=0.001:
            Kprecision/=10
        maxK=K
        maxT=T+Tprecision
        K+=Kprecision
        T+=Tprecision
    elif G(K+Kprecision,T+Tprecision)<=maxG and G(K+Kprecision,T)>maxG:
        maxG=G(K+Kprecision,T)
        T-=Tprecision
        if Tprecision>=0.001:
            Tprecision/=10
        maxK=K+Kprecision
        maxT=T
        K+=Kprecision
        T+=Tprecision
    elif G(K+Kprecision,T+Tprecision)<=maxG and G(K,T)>maxG:
        maxG=G(K,T)
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
"""
