from functools import reduce
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # ord(0) = 48, ord(9) = 57
        convert_to_digit = lambda x: ord(x) - 48
        converge_to_num = lambda a, b: a * 10 + b
        num1 = reduce(converge_to_num, map(convert_to_digit, num1))
        num2 = reduce(converge_to_num, map(convert_to_digit, num2))
        return str(num1 * num2)
    
num1 = "2"
num2 = "3"
print(Solution().multiply(num1, num2))
num1 = "123"
num2 = "456"
print(Solution().multiply(num1, num2))