class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            
            if nums[i] in hash:
                return [hash[nums[i]], i]

            hash[comp] = i
