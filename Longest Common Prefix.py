#最长共用前缀字符串

class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs)==0 or strs==None :
            return ''

        z = zip(*strs)

        for i,group in enumerate(z):
            print(group)

        l = list(strs)
        compare=l[0]

        for i in range(1,len(l)):
            tmp=l[i]
            while len(compare)>0:
                if str(tmp).startswith(compare):
                    break
                else:
                    compare=compare[0:len(compare)-1]

        return compare

    def longestCommonPrefix2(self, strs):
        return 0





so=Solution()
target=['123','1223565456','12356544','1236756787']
res=so.longestCommonPrefix(target)
print(res)
