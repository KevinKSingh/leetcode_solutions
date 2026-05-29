class Solution:
    def minElement(self, nums: List[int]) -> int:
        my_list = [str(x) for x in nums]
        my_list_2 = []
        for item in my_list:
            my_sum = 0
            for char in item:
                my_sum += int(char)
            my_list_2.append(my_sum)
        return min(my_list_2)
