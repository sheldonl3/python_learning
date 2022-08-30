#纸币找0
class Solution:
    def GetCoinCount(self , N ):
        n64=(1024-N)//64
        n16=((1024-N)%64)//16
        n4=(((1024-N)%64)%16)//4
        n1=(1024-N)-n64*64-n16*16-n4*4
        return n4+n1+n16+n64

if __name__=='__main__':
    s=Solution()
    print(s.GetCoinCount(200))
