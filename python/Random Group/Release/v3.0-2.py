def group():
    import random
    name=["申思远","潘虹阳","张泽阳","明子涵","张乐","王方铭","黄俊杰","张奥","陈彦博","曾天泽","高源","孙泽林","卡米力·万里","杨凌杰","焦博君","刘清扬","余沛瑶","赵怡然","张璇","唐予珊","金芝贤","陈艺嘉"]
    gpa=[]
    gpb=[]
    gpc=[]
    gpd=[]
    for i in range(5):
        a=random.choice(name)
        name.remove(a)
        gpa.append(a)
    for i in range(5):
        a=random.choice(name)
        name.remove(a)
        gpb.append(a)
    for i in range(6):
        a=random.choice(name)
        name.remove(a)
        gpc.append(a)
    for i in range(6):
        a=random.choice(name)
        name.remove(a)
        gpd.append(a)
    print("第一组人员: {0}, {1}, {2}, {3}, {4}".format(gpa[0],gpa[1],gpa[2],gpa[3],gpa[4]))
    print("第二组人员: {0}, {1}, {2}, {3}, {4}".format(gpb[0],gpb[1],gpb[2],gpb[3],gpb[4]))
    print("第三组人员: {0}, {1}, {2}, {3}, {4}, {5}".format(gpc[0],gpc[1],gpc[2],gpc[3],gpc[4],gpc[5]))
    print("第四组人员: {0}, {1}, {2}, {3}, {4}, {5}".format(gpd[0],gpd[1],gpd[2],gpd[3],gpd[4],gpd[5]))
    print()
