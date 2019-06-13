def randomgroup(x):
    import random
    
    list1=["申思远","潘虹阳","张泽阳","明子涵","张乐","黄俊杰","张奥","陈彦博","曾天泽","高源","卡米力·万里","杨凌杰"]
    list2=["焦博君","赵怡然","张璇","唐予珊","金芝贤","陈艺嘉"]

    if 2<=x<=11:
        if x==2:
            a=random.choice(list1)
            list1.remove(a)
            b=random.choice(list1)
            list1.remove(b)
            c=random.choice(list1)
            list1.remove(c)
            d=random.choice(list1)
            list1.remove(d)
            e=random.choice(list1)
            list1.remove(e)
            f=random.choice(list1)
            list1.remove(f)
            h=random.choice(list2)
            list2.remove(h)
            i=random.choice(list2)
            list2.remove(i)
            j=random.choice(list2)
            list2.remove(j)

            l=random.choice(list1)
            list1.remove(l)
            m=random.choice(list1)
            list1.remove(m)
            n=random.choice(list1)
            list1.remove(n)
            o=random.choice(list1)
            list1.remove(o)
            p=random.choice(list1)
            list1.remove(p)
            q=random.choice(list1)
            list1.remove(q)
            t=random.choice(list2)
            list2.remove(t)
            u=random.choice(list2)
            list2.remove(u)
            v=random.choice(list2)
            list2.remove(v)

            print("第一组成员\n   {0}\n   {1}\n   {2}\n   {3}\n   {4}\n   {5}\n   {6}\n   {7}\n   {8}".format(a,b,c,d,e,f,h,i,j))
            print("第二组成员\n   {0}\n   {1}\n   {2}\n   {3}\n   {4}\n   {5}\n   {6}\n   {7}\n   {8}".format(l,m,n,o,p,q,t,u,v))
            
        if x==5:
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

            print("第一组成员\n   {0}\n   {1}\n   {2}\n   {3}".format(a,b,c,d))
            print("第二组成员\n   {0}\n   {1}\n   {2}\n   {3}".format(e,f,g,h))
            print("第三组成员\n   {0}\n   {1}\n   {2}\n   {3}".format(i,j,k,l))
            print("第四组成员\n   {0}\n   {1}\n   {2}\n   {3}\n   {4}".format(m,n,o,p,q))
            print("第五组成员\n   {0}\n   {1}\n   {2}\n   {3}\n   {4}".format(r,s,t,u,v))

        else:
            return
        
    else:
        return
