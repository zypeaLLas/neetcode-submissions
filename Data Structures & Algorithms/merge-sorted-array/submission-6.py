class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # if(m == 0 and n ==0):
        #     return
        # if(n == 0):
        #     nums1.sort()
        #     return
        # #merge the lists
        # i,j = m, 0

        # while i < (m + n) and j < n:
        #     nums1[i] = nums2[j]
        #     i+=1
        #     j+=1
        # nums1.sort()
        # return

        """
        TWO LINE SOLUTION
        """
        nums1[m:] = nums2
        nums1.sort()
        