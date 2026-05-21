class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashset= set()
        l = 0
        hashset.add(nums[0])
        for r in range(1, len(nums)):
            if (r - l) > k:
                hashset.remove(nums[l])
                l +=1
            if nums[r] in hashset:
                return True
            hashset.add(nums[r])
        return False