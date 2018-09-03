def insert_sort(list):
    for i in range(1,len(list)):
        x = list(i) #取到要插入的数
        j = i  #取到要插入的数的索引
        while j>0 and list[j-1]>x: #如果索引小的值比索引大的值大
            list[j] = list[j-1] #依次后移
            j-=1  
        list[j] = x   #此时的j即为要插入的位置索引
        
