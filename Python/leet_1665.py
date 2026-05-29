class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # Sort by the "saved" effort (minimum - actual) descending
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        
        current_effort = 0
        total_required = 0
        
        for actual, minimum in tasks:
            if total_required < minimum:
                # We need to increase our starting energy to meet this minimum
                current_effort += (minimum - total_required)
                total_required = minimum
            
            # Spend the actual energy
            total_required -= actual
            
        return current_effort
        
        
