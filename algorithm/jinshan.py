def work(N):
    if N == 0:
        return
    if N == 1:
        print(1)
        return
    if N == 2:
        tmp=[1,1,1]
        print(1)
        for each in tmp:
            print(each, end=' ')
        return
    tmp = [1, 1, 1]
    print(1)
    for each in tmp:
        print(each, end=' ')
    a, b = 1, 1
    lis = [1, 1]
    for _ in range(N - 2):
        a, b = b, a + b
        lis.append(b)
        l = len(lis)
        left = lis[:l - 1]
        left.reverse()
        tmp = lis + left
        # print(tmp)
        for each in tmp:
            print(each, end=' ')
        print()
    return


if __name__ == "__main__":
    s = int(input())
    work(s)
