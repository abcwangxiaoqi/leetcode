#回文数 正读反读都一样
#解决思路 用模的方式 取余数 反写出了 比较

class Solution(object):

    #反读和原数对比
    def isPalindrome1(self, num):
        """
        :type x: int
        :rtype: bool
        """
        if num<0:
            return False

        if num<10:
            return True

        s = 0
        bNum = num
        mod= 0

        while bNum!=0:
            mod=bNum%10
            print('mod=',mod)
            s=s*10+mod
            print('s=', s)
            bNum=int(bNum/10)
            print('bNum=', bNum)
        res=(s==num)
        return res

    #反读读取一般对比 效率更高
    def isPalindrome2(self,num):
        if num<0:
            return False
        if num<10:
            return True

        cur=0

        while num > cur:
            cur = cur*10 + num % 10
            num = int(num/10)

        return ( num == cur or num == int(cur / 10) )


so=Solution()
target=1001
result=so.isPalindrome2(target)
print(result)