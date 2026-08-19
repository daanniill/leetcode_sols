class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if nums[i] in hash:
                return [hash[nums[i]], i]
            

            hash[complement] = i
