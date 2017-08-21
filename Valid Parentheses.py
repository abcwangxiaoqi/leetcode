#验证匹配括号

class Solution(object):

    def bestIsValid(self,s):

        #进栈出栈方式来验证匹配

        stack=[]

        for char in s:
            if char=="(":
                stack.append(")")
            elif char=="[":
                stack.append("]")
            elif char=="{":
                stack.append("}")
            elif stack==[] or stack.pop()!=char:
                return False

        return stack==[]

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """


        if len(s)<2:
            return False

        temp1="()"
        temp2="{}"
        temp3="[]"

        while len(s)>0:
            if temp1 in s:
                s=s.replace(temp1,"")
            elif temp2 in s:
                s=s.replace(temp2, "")
            elif temp3 in s:
                s=s.replace(temp3, "")
            else:
                return False
                break
        return True


so=Solution()
str="([{])"
res=so.bestIsValid(str)
print(res)