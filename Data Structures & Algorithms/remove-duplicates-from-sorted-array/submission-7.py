class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # i=0
        # while i < len(nums)-1:
        #     j=i+1
        #     while j < len(nums):
        #         if nums[i] == nums[j]:
        #             nums.pop(j)
        #         else: #need else, we can't just i+=1 after popping -> missing an element.
        #             # j+=1  sorted already so if it's different -> all the next elements are different. so break.
        #             break
        #     i+=1
        # return len(nums)
        unique = sorted(set(nums))
        nums[:len(unique)] = unique
        return len(unique)