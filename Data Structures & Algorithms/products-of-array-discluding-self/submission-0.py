class Solution:
    def calculate(self, index: int, nums: List[int]):
        product = 1
        for i in range(len(nums)):
            if(i == index): continue
            product *= nums[i]
        return product
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            res.append(self.calculate(i, nums))
        return res