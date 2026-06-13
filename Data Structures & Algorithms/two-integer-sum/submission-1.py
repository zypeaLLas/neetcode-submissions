class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # map={}
        # for i, n in enumerate(nums):
        #     map[n] = i

        # for i, n in enumerate(nums):
        #     complement=target - n
        #     if complement in map and map[complement] != i:
        #         return [i,map[complement]]
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

        return