# 将 123转换为321  -123转为-321

class Solution(object):

    def myReverse(self,x):

        moreZero=True
        if x<0:
            moreZero=False
            x=x*-1

        result=0
        l=len(str(x))
        cou=1;
        while x:
            x,r=divmod(x,10)
            result=r*(pow(10,l-cou))+result
            cou=cou+1

        if moreZero==False:
            result=result*-1

        Int32_Max=2147483647
        Int32_Min=-2147483648
        if result>Int32_Max:
            return 0
        if result<Int32_Min:
            return 0
        return result

target=1534236469
so=Solution()
result=so.myReverse(target)
print(result)