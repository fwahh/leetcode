class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {n}
        while n != 1:
            n = sum(map(lambda x: int(x)**2, str(n)))
            if n in seen:
                return False
            seen.add(n)
        
        return True