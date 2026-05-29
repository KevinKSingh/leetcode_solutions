class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        l, r = 0,0
        min_length = min(len(nums1), len(nums2))
        while l < len(nums1) and r < len(nums2):
            l_num, r_num = nums1[l], nums2[r]
            print(l_num, r_num)
            if l_num > r_num:
                r += 1
            elif r_num > l_num:
                l += 1
            elif r_num == l_num:
                return l_num
        return -1
