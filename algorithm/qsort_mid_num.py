# 用快排找中位数
def qsort_find(array,left,right,mid_index):           #用快排找下标mid_index的数
    if(left>=right):
        return array[left]
    lp=left
    rp=right
    key=array[left]
    while lp<rp:
        while (array[rp] >= key) and (lp < rp):
            rp -= 1
        while (array[lp]<=key) and (lp<rp):
            lp+=1
        array[lp],array[rp]=array[rp],array[lp]
    array[lp],array[left]=array[left],array[lp] #lp是一趟排序可以确定的index，他是mid的话array[lp]就是要找的数
    if lp==mid_index:
        return array[lp]
    elif lp>mid_index:                         #不是的话进行剪枝
        return qsort_find(array,left,lp-1,mid_index)
    return qsort_find(array,lp+1,right,mid_index)

def quick_sort_mid(array):
    l=len(array)
    if l==0:
        return
    mid=l//2
    if l%2==0:          #偶数找2次算平均，奇数找1次
        return (qsort_find(array, 0, len(array) - 1,mid)+qsort_find(array, 0, len(array) - 1,mid-1))/2
    else:
        return qsort_find(array, 0, len(array) - 1,mid)

if __name__=='__main__':
    array = [1,5,0]
    a=quick_sort_mid(array)
    print(a)