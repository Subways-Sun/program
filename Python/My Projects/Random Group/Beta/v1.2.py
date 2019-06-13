def randomgroup2(a):
    import random
    list1=["申思远","潘虹阳","张泽阳","明子涵","张乐","王方铭","黄俊杰","张奥","陈彦博","曾天泽","高源","孙泽林","卡米力·万里","杨凌杰"]
    list2=["焦博君","刘清扬","余沛瑶","赵怡然","张璇","唐予珊","金芝贤","陈艺嘉"]
    print("第一组成员:")
    male=14//a
    female=8//a
    for i in range(male):
        f=random.choice(list1)
        list1.remove(f)
        print(f)
    for i in range(female):
        g=random.choice(list2)
        list2.remove(g)
        print(g)
    print("第二组成员:")
