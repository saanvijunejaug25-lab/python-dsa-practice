class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi =sum(nums)
        for i in range(len(nums)):
            total = 0
            for j in range(i,len(nums)):
                total = total + nums[j]
                if total>maxi:
                    maxi = total
        return maxi

        