#题意是n=1时输出字符串1；
# n=2时，数上次字符串中的数值个数，因为上次字符串有1个1，所以输出11；
# n=3时，由于上次字符是11，有2个1，所以输出21；n=4时，由于上次字符串是21，有1个2和1个1，所以输出1211。
# 依次类推，写个countAndSay(n)函数返回字符串

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res='1'
        cur=1

        if n<cur:
            return None

        while cur<n:
            res=self.OutRes(res)
            cur+=1
        return res

    def OutRes(self, strs):

        res=''
        tmpNum=None
        tmpNumCou=0

        for i in range(len(strs)):
            if tmpNum != strs[i]:
                if tmpNumCou > 0 and tmpNum != None:
                    res += str(tmpNumCou)
                    res += tmpNum
                tmpNumCou = 1
                tmpNum = strs[i]
            else:
                tmpNumCou += 1

            if i==len(strs)-1:
                res += str(tmpNumCou)
                res += tmpNum
        return res

target=5
so=Solution()
res=so.countAndSay(target)
print(res)