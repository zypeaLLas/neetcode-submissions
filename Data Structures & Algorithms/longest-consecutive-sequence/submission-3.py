class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """Brute force solution"""
        """find min
        then iterate through the list to check if min + 1 exist, add the valid elements -> res[]
        -> len(res)
"""
        if not nums: return 0
        res = 0
        hashset  = set(nums)
        for num in nums:
            streak, num2 = 0, num
            while num2 in hashset:
                streak +=1
                num2 +=1
            if res < streak:
                res = streak
        return res

        """Hash map solution"""
        # mp = defaultdict(int)
        # res = 0

        # for num in nums:
        #     if not mp[num]:
        #         mp[num] = mp[num - 1] + mp[num + 1] + 1
        #         mp[num - mp[num - 1]] = mp[num]
        #         mp[num + mp[num + 1]] = mp[num]
        #         res = max(res, mp[num])
        # return res