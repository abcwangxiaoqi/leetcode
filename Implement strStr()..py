#判断字符串是否是另外一个字符串的子集 如果存在返回index 如果不存在返回-1

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if haystack==needle:
            return 0
        index = -1
        stackL=len(haystack)
        needleL=len(needle)
        if needleL>stackL:
            return index

        for i in range(0,stackL-needleL+1):
            if haystack[i] == needle[0] and haystack[i:i+needleL]==needle:
                    index=i
                    break
        return index



stack=''
needle=''
so=Solution()
res=so.strStr(stack,needle)
print(res)
