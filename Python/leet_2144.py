class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        #print(cost)
        my_candies = []
        idx = 0
        if len(cost) <= 2:
            return sum(cost)
        for idx, var in enumerate(cost):
            if (idx+1)%3==0:
                continue
            else:
                my_candies.append(var)
        return sum(my_candies)
