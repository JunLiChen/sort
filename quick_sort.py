def quick_sort(lst,l,r):
    if l>= r:
        return
    i = 1
    j = r
    pivot = lst[i]
    while i<j:
        while i<j and lst[j]>=pivot:
            j-=1
        if i<j:
            lst[i] = lst[j]
            i+=1
        while i<j and lst[i]<=pivot:
            i+=1
        if i<j:
            lst[j] = lst[i]
            j-=1
    quick_sort(lst,1,i-1)
    quick_sort(lst,i+1,r)
