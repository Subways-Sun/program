def randomgroup(x):
    import random
    if 2<=x<=11:
        list1=["申思远","潘虹阳","张泽阳","明子涵","张乐","王方铭","黄俊杰","张奥","陈彦博","曾天泽","高源","孙泽林","卡米力·万里","杨凌杰"]
        list2=["焦博君","刘清扬","余沛瑶","赵怡然","张璇","唐予珊","金芝贤","陈艺嘉"]

        a1="王方铭"
        a2="卡米力·万里"

        if x==2:
            list3m=[]
            list3w=[]
            list4m=[]
            list4w=[]
            list5=[]
            list6=[]

            list1.remove(a1)
            list1.remove(a2)

            list=[3,4]
            gn=random.choice(list)
            if gn==3:
                list3m.append(a1)
                list3m.append(a2)
            if gn==4:
                list4m.append(a1)
                list4m.append(a2)

            while len(list1)>0:
                a=random.choice(list1)
                list5.append(a)
                list1.remove(a)
            while len(list2)>0:
                a=random.choice(list2)
                list6.append(a)
                list2.remove(a)

            while len(list3m)<7:
                a=list5[0]
                list5.remove(a)
                list3m.append(a)
            while len(list3w)<4:
                a=list6[0]
                list6.remove(a)
                list3w.append(a)
            while len(list4m)<7:
                a=list5[0]
                list5.remove(a)
                list4m.append(a)
            while len(list4w)<4:
                a=list6[0]
                list6.remove(a)
                list4w.append(a)

            list3=list3m+list3w
            list4=list4m+list4w

            print("第一组成员\n   {0}\n   {1}\n   {2}\n   {3}\n   {4}\n   {5}\n   {6}\n   {7}\n   {8}\n   {9}\n   {10}".format(list3[0],list3[1],list3[2],list3[3],list3[4],list3[5],list3[6],list3[7],list3[8],list3[9],list3[10]))
            print("第二组成员\n   {0}\n   {1}\n   {2}\n   {3}\n   {4}\n   {5}\n   {6}\n   {7}\n   {8}\n   {9}\n   {10}".format(list4[0],list4[1],list4[2],list4[3],list4[4],list4[5],list4[6],list4[7],list4[8],list4[9],list4[10]))
                
        if x==5:
            list3m=[]
            list3w=[]
            list4m=[]
            list4w=[]
            list5m=[]
            list5w=[]
            list6m=[]
            list6w=[]
            list7m=[]
            list7w=[]
            list8=[]
            list9=[]

            list1.remove(a1)
            list1.remove(a2)
            
            list=[3,4,5,6,7]
            gn=random.choice(list)
            if gn==3:
                list3m.append(a1)
                list3m.append(a2)
            if gn==4:
                list4m.append(a1)
                list4m.append(a2)
            if gn==5:
                list5m.append(a1)
                list5m.append(a2)
            if gn==6:
                list6m.append(a1)
                list6m.append(a2)
            if gn==7:
                list7m.append(a1)
                list7m.append(a2)

            while len(list1)>0:
                a=random.choice(list1)
                list1.remove(a)
                list8.append(a)
            while len(list2)>0:
                a=random.choice(list2)
                list2.remove(a)
                list9.append(a)
                
            while len(list3m)<3:
                a=list8[0]
                list8.remove(a)
                list3m.append(a)
            while len(list3w)<1:
                a=list9[0]
                list9.remove(a)
                list3w.append(a)
            while len(list4m)<3:
                a=list8[0]
                list8.remove(a)
                list4m.append(a)
            while len(list4w)<1:
                a=list9[0]
                list9.remove(a)
                list4w.append(a)
            while len(list5m)<2:
                a=list8[0]
                list8.remove(a)
                list5m.append(a)
            while len(list5w)<2:
                a=list9[0]
                list9.remove(a)
                list5w.append(a)
            while len(list6m)<3:
                a=list8[0]
                list8.remove(a)
                list6m.append(a)
            while len(list6w)<2:
                a=list9[0]
                list9.remove(a)
                list6w.append(a)
            while len(list7m)<3:
                a=list8[0]
                list8.remove(a)
                list7m.append(a)
            while len(list7w)<2:
                a=list9[0]
                list9.remove(a)
                list7w.append(a)

            list3=list3m+list3w
            list4=list4m+list4w
            list5=list5m+list5w
            list6=list6m+list6w
            list7=list7m+list7w

            print("第一组成员\n   {0}\n   {1}\n   {2}\n   {3}".format(list3[0],list3[1],list3[2],list3[3]))
            print("第二组成员\n   {0}\n   {1}\n   {2}\n   {3}".format(list4[0],list4[1],list4[2],list4[3]))
            print("第三组成员\n   {0}\n   {1}\n   {2}\n   {3}".format(list5[0],list5[1],list5[2],list5[3]))
            print("第四组成员\n   {0}\n   {1}\n   {2}\n   {3}\n   {4}".format(list6[0],list6[1],list6[2],list6[3],list6[4]))
            print("第五组成员\n   {0}\n   {1}\n   {2}\n   {3}\n   {4}".format(list7[0],list7[1],list7[2],list7[3],list7[4]))
            
        else:
            return

    else:
        return
