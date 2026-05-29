class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        my_list = []
        for n in nums:
            my_list.append(n*n)
        my_list.sort()
        return my_list
        
