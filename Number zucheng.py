# 0到9 有多少可以组成多少组不同的2位数
# 排列组合 允许相同--十位数:可以有1~9 9种 个位数:可以有0~9 10种 总共9*10=90种
#         不允许相同--十位数:可以有1~9 9种 个位数:可以有0~9 10种，不允许相同-1，个位数可以有9种 总共9*9=81种
class Solution(object):
    def OutResult(self,same,cou):
        #0~9 作为原始数据
        #same 是否允许相同数字出现
        #cou 组成几位数 必须大于0


        if cou<=0:
            return False

        if cou==1:
            return 10

        total=None
        i=1
        while cou>0:
            if total==None:
                total=10-1#首位不能出现0
            else:
                if same:
                    total=total*10
                else:
                    total=total*(10-i)
                i += 1

            cou-=1

        return total



so=Solution()
res=so.OutResult(True,3)

print(res)

