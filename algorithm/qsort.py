def quick_sort(array):
    res = qsort(array,0,len(array)-1)
    return res

def qsort(array,left,right):
    if(left>=right):
        return array
    lp=left
    rp=right
    key=array[left]
    while lp<rp:
        while (array[rp] >= key) and (lp < rp):
            rp -= 1
        while (array[lp]<=key) and (lp<rp):
            lp+=1
        array[lp],array[rp]=array[rp],array[lp]
    array[lp],array[left]=array[left],array[lp]
    qsort(array,left,lp-1)
    qsort(array,rp+1,right)
    return array


if __name__=='__main__':
    array = [5, 40, 2, 4, 55, 6, 5, 34, 656, 978]
    a=quick_sort(array)
    print(a)