'''给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
'''
def work(s):
    stack=[-1]
    res=0
    for i,x in enumerate(s):
        if x=='(':
            stack.append(i)
        else:
            stack.pop()
            if stack:
                res=max(res, i-stack[-1])
            else:
                stack.append(i)
    return res

'''
给定一个正整数n，找出与其二进制表达式中1的个数相同且大小最接近的那两个数（一个略大，一个略小）。
'''
def findNumber(num):
    c0=0
    c1=0
    c=num
    while c&1==0 and c!=0:
        c0+=1
        c>>=1
    while c&1==1:
        c1+=1
        c>>=1
    if c0+c1==31 or c0+c1==0:
        return -1
    p=c0+c1
    num|=(1<<p)
    num&=~((1<<p)-1)
    num|=(1<<(c1-1))-1
    return num

def getprv(num):
    tmp=num
    c0=0
    c1=0
    while tmp&1==1:
        c1+=1
        tmp>>=1
    if tmp==0:
        return -1
    while tmp&1==0 and tmp!=0:
        c0+=1
        tmp>>=1
    p=c0+c1
    num&=((~0)<<(p+1))
    mask=(1<<(c1+1))-1
    num|=mask<<(c0-1)
    return num

'''
jinwei
'''
_base32='0123456789dcdefghj'

if __name__ == '__main__':
    print(findNumber(2))
    print(getprv(2))
