class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        i=0
        while i < (len(nums)-1):
            j=i+1
            while j < len(nums):
                if(nums[i] == nums[j]):
                    nums.pop(j)
                else: #need else, we can't just i+=1 after popping -> missing an element.
                    j+=1
            i+=1
        count = 0
        for value in nums:
            count +=1
        return count