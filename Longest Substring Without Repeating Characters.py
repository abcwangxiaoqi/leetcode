#找出字符串中不重复字符串最大的长度

#算法思想
#定义一个 起始指针start，定义一个结束指针end，start和end之间作为最优解的数组
#过程：end指针向后走，如果遇到重复字符串则停止，计算得出最优解，然后start指针指向重复数字的后一位，end继续向后走，以次轮询最后得出最优解
#核心思想：贪心算法
#

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                #得出计算索引
                start = usedChar[s[i]] + 1
            else:
                #得出最大值
                maxLength = max(maxLength, i - start + 1)
            #赋值字典
            usedChar[s[i]] = i
        return maxLength

    def mylength(self,s):
        maxL=0
        start=0

        map={}

        for i in range(len(s)):
            #陷阱：重新开始扫描的位置 start要小于map里面记录的标记 否则start位置错误
            if s[i] in map and start<=map[s[i]]:
                #得出重复字符串，start指针指向重复字符串的后一位
                start=map[s[i]]+1
                print('start=',start)
            else:
                #得出最优解的长度
                maxL=max(maxL,i-start+1)
                print('maxL=', maxL)

            #记录扫描过的字符串
            map[s[i]] = i
        return maxL

str='tmmzuxt'
#str='w'
so=Solution()
#res=so.lengthOfLongestSubstring(str)
res=so.mylength(str)
print('res=',res)

#map 每个字母当key