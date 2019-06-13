def randomgroup2():
        import random
        list1=["申思远","潘虹阳","张泽阳","明子涵","张乐","王方铭","黄俊杰","张奥","陈彦博","曾天泽","高源","孙泽林","卡米力·万里","杨凌杰"]
        list2=["焦博君","刘清扬","余沛瑶","赵怡然","张璇","唐予珊","金芝贤","陈艺嘉"]
        for i in range(10):
            a=random.choice(list1)
            list1.remove(a)
            b=random.choice(list1)
            list1.remove(b)
            c=random.choice(list1)
            list1.remove(c)
            d=random.choice(list2)
            list2.remove(d)
                
                e=random.choice(list1)
                list1.remove(e)
                f=random.choice(list1)
                list1.remove(f)
                g=random.choice(list1)
                list1.remove(g)
                h=random.choice(list2)
                list2.remove(h)
                
                i=random.choice(list1)
                list1.remove(i)
                j=random.choice(list1)
                list1.remove(j)
                k=random.choice(list2)
                list2.remove(k)
                l=random.choice(list2)
                list2.remove(l)

                m=random.choice(list1)
                list1.remove(m)
                n=random.choice(list1)
                list1.remove(n)
                o=random.choice(list1)
                list1.remove(o)
                p=random.choice(list2)
                list2.remove(p)
                q=random.choice(list2)
                list2.remove(q)

                r=random.choice(list1)
                list1.remove(r)
                s=random.choice(list1)
                list1.remove(s)
                t=random.choice(list1)
                list1.remove(t)
                u=random.choice(list2)
                list2.remove(u)
                v=random.choice(list2)
                list2.remove(v)
            
                list3=[a,b,c,d]
                list4=[e,f,g,h]
                list5=[i,j,k,l]
                list6=[m,n,o,p,q]
                list7=[r,s,t,u,v]

                if list3.count("张奥")+list3.count("卡米力·万里")<2:
                    return
                if list4.count("张奥")+list4.count("卡米力·万里")<2:
                    return
                if list5.count("张奥")+list5.count("卡米力·万里")<2:
                    return
                if list6.count("张奥")+list6.count("卡米力·万里")<2:
                    return
                if list7.count("张奥")+list7.count("卡米力·万里")<2:
                    return

                print(list3)
