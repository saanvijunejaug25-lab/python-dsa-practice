class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        high = nums[0]
        for i in range(len(nums)):
            product = 1
            for j in range(i,len(nums)):
                product = product* nums[j]
                if product>high:
                    high = product
        return high
        