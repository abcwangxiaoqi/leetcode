#Given a sorted array and a target value,
# return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

#You may assume no duplicates in the array.

#Here are few examples.
#[1,3,5,6], 5 → 2
#[1,3,5,6], 2 → 1
#[1,3,5,6], 7 → 4
#[1,3,5,6], 0 → 0

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        res=len(nums)

        for i in range(res):
            if nums[i]>=target:
                res=i
                break

        return res


target=50
nums=[1,3,5,9,6,88,66]
so=Solution()
res=so.searchInsert(nums,target)
print(res)
