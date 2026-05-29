class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        my_set = list(set(nums))
        my_dict = {k: 0 for k in my_set}
        for var in nums:
            my_dict[var] += 1
        #test_dict = {k: v for k, v in my_dict.items() if v == 1}
        target_key = next((k for k, v in my_dict.items() if v == 1), None)
        return target_key
        
