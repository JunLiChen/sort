def select_sort(lst):
    for i in range(len(lst)-1):
        k = i  #
        for j in range(i,len(lst)):
            if(lst[j]<lst(k)):
                k = j  #k是此轮找出的最小值的索引
        if(k!=i):    
            lst[i],lst[k] = lst[k],lst[i]
        
