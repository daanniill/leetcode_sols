class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, right = 0, len(nums) - 1

        while l <= right:
            m = (l + right) // 2

            if nums[m] == target:
                return m
            elif nums[m] > target:
                right = m - 1
            else:
                l = m + 1
        
        return l
