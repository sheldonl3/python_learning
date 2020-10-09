import array

def littleorbig():
    lis=array.array('h',[1]).tobytes()
    print(lis)
    if lis[0]==1:
        print('small')
        return
    print('high')

if __name__=='__main__':
    littleorbig()