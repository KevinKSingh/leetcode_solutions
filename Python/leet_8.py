class Solution:
    def myAtoi(self, s: str) -> int:
        my_int = s.strip()
        if not my_int:
            return 0
        factor = 1
        if my_int[0] == '-':
            factor = -1
            my_int = my_int[1:]
        elif my_int[0] == '+':
            my_int = my_int[1:]
            
        my_answer = 0
        
        for char in my_int:
            if '0' <= char <= '9':
                my_answer = my_answer * 10 + (ord(char) - ord('0'))
            else:
                break
                
        final_result = factor * my_answer
        
        if final_result < -2**31:
            return -2**31
        if final_result > 2**31 - 1:
            return 2**31 - 1
            
        return final_result
