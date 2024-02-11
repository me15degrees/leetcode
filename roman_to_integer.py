class Solution:
    def romanToInt(self, s: str) -> int:   
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        prev_value = 0
        
        for i in range(len(s) - 1, -1, -1):
            curr_value = roman_values[s[i]]
            if curr_value >= prev_value:
                sum += curr_value
            else:
                sum -= curr_value
            prev_value = curr_value
        
        return sum