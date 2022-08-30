'''
10 3
3
2
2
2
3
4
4
1
1
0
'''


def do(dic, num):
    dic_ci = {}
    for k, v in dic.items():
        if v not in dic_ci:
            dic_ci[v] = [k]
        else:
            dic_ci[v].append(k)
    for k, v in dic_ci.items():
        v.sort()
    dic_ci_sort = sorted(dic_ci)  # 对key单独排序，输出之后的list
    # dic_test={1:'ads',2:'ret',3:'ags'}#对value排序，输出之后的tuple
    # print(sorted(dic_test.items(), key=lambda item: item[1]))

    print(dic)
    print(dic_ci)
    print(dic_ci_sort)
    # print(dic_ci_sort_dic)
    i = 0
    for k in dic_ci_sort[::-1]:
        if i >= num:
            break
        for each in dic_ci[k]:
            print(each, k)
            i += 1
            if i >= num:
                break
    i = 0
    for k in dic_ci_sort:
        if i >= num:
            break
        for each in dic_ci[k]:
            print(each, k)
            i += 1
            if i >= num:
                break


if __name__ == '__main__':
    a = [int(i) for i in input().split()]
    dic = {}
    for _ in range(a[0]):
        b = input()
        if b not in dic:
            dic[b] = 1
        else:
            dic[b] += 1
    do(dic, a[1])
