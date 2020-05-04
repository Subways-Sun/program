from sympy
A=float() # 用户体验
K=float() # 门槛值
T=int() # 关闭周期时长
Qi=list() # 每种用电器的使用率
Ci=list() # 每种用电器的使用连贯性
H=24*3600//T # 每天总检测周期数
f=list() # 瞬时检测频率 len(f)==H
U=int() # 总用户数
Mi=list() # 每种用电器关闭个数 len(Mi)==len(Pi)
ti=list() # 每种用电器每天平均使用时间(s) len(ti)==len(Pi)
Pi=list() # 每种用电器功率值(每个电器由其功率值代表)
Zi=list() # 电网范围内某种电器占有率
Vi=list() # 每个用户拥有多少此类用电器
Di=list() # 每种用电器的需求评分 len(Di)==len(Pi) Range:[0,10]
Yi=list() # 每种用电器的调节常数 len(Yi)=len(Pi) Range:[0,1]
di=list() # 每种用电器开/关 len(di)==H len(di[i])==len(Pi) 初始化di
Ni=list() # 每种用电器每天关闭周期数 Ni<=H
Bi=list() # 每种用电器每天关闭次数 Bi<=Ni<=H
S=50-K # 门槛频率
fh=S+K*0.25 # 调节目标频率
Ptotal=list() # 每种用电器的总有效功率值
for i in range(len(Pi)):
    Ptotal.append(Pi[i]*U*Zi[i]*Vi[i])
for i in range(H): # 针对每次调频，确定每类用电器是否关闭
    Pl=0
    di.append([])
    for j in range(len(Pi)):
        di[i+1].append(1)
    for j in range(len(Pi)): # 针对每种用电器计算调频前总功率
        Pl+=Ptotal[j]*di[i][j]
    deltaPj=((fh/50-f[i]/50)*Kl)/(1-(1-fh/50)*Kl)*Pl
    index=[] # 停机列表(在Pi中的序号)
    Ptotalt=Ptotal # 创建可选用电器列表，防止原始列表被改动
    for j in range(len(Pi)):
        diff=[[],[]] # 寻找与减载量最相近的负荷
        for k in range(len(Pi)-j): # 针对每种用电器计算与减载量的差值
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
for i in range(len(Pi)): # 计算电器使用率Qi
    if Ni[i]*T>ti[i]:
        Qi.append(0)
    else:
        Qi.append((ti[i]-Ni[i]*T)/ti[i])
for i in range(len(Pi)): # 计算连贯性Ci
    if Ni[i]==0:
        Ci.append(1)
    else:
        Ci.append((Ni[i]-(Bi[i]*Yi[i]))/Ni[i])
for i in range(len(Pi)): # 计算用户体验A
    A+=Di[i]*Yi[i]*(0.5*Qi[i]+0.5*Ci[i])*Ni[i]
