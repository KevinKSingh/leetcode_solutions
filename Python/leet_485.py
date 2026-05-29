class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        my_counter = 0
        max_counter = 0
        for num in nums:
            if num == 1:
                my_counter += 1
                max_counter = max(my_counter, max_counter)
            else:
                max_counter = max(my_counter, max_counter)
                my_counter = 0
        return max_counter
