# 如何将难度从 n*n 降为 n，合理利用字典降低维度


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        result = []
        for i in range(len(nums)):
            if nums[i] in map:
                result = [i, map[nums[i]]]
                return result
            else:
                map[target - nums[i]] = i

nums=[1,2,3,4,5,6]
target=9
so=Solution()
result =so.twoSum(nums,target)
print(result)
