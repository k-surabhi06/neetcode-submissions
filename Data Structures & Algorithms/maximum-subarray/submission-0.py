class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        largest_sum = nums[0]
        for i in range(1,len(nums)):
            current_sum = max(nums[i],nums[i]+current_sum)
            largest_sum = max(largest_sum,current_sum)
        return largest_sum