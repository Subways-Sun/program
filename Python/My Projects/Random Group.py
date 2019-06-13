def randomgroup():
    import random
    together=["申思远","潘虹阳","张泽阳","明子涵","张乐","王方铭","黄俊杰","张奥","陈彦博","曾天泽","高源","孙泽林","卡米力·万里","杨凌杰","焦博君","刘清扬","余沛瑶","赵怡然","张璇","唐予珊","金芝贤","陈艺嘉"]
    boy=["申思远","潘虹阳","张泽阳","明子涵","张乐","王方铭","黄俊杰","张奥","陈彦博","曾天泽","高源","孙泽林","卡米力·万里","杨凌杰"]
    girl=["焦博君","刘清扬","余沛瑶","赵怡然","张璇","唐予珊","金芝贤","陈艺嘉"]
    sepa=input("Are boys and girls calculated separately?\n")
    try:
        if sepa=='Yes':
            
        elif sepa=='No' or sepa==None:
            sp=0
        else:
            raise ReferenceError            
