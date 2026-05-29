class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        my_list = []
        for n in nums:
            for m in str(n):
                my_list.append(int(m))
        return my_list
        
