
from collections import Counter
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        my_dict = Counter(nums)
        l1, l2 = [], []
        single = list(filter(lambda key: my_dict[key] == 1, my_dict))
        l1 = single[0:len(single)//2]
        l2 = single[len(single)//2:]
        for key in my_dict:
            if my_dict[key] > 2:
                return False
            if my_dict[key] == 2:
                l1.append(my_dict[key]), l2.append(my_dict[key])
        return True
