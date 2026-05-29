import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()
        l, r = 1, max(nums)
        factor = []
        minSum = float('inf')
        while l < r:
            mid = (l+r)//2
            my_sum = sum(math.ceil(x/mid) for x in nums)
            minSum = min(my_sum, minSum)
            factor.append(mid)
            #print(nums, l, r, mid, my_sum, minSum)
            if my_sum > threshold:
                l = mid + 1
            else:
                r = mid
        return l
        
           
