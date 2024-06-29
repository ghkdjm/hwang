class Solution:
    def isHappy(self, n: int) -> bool:
        end = set()
        while n != 1:
            sum = 0
            while n > 0:
                digit = n % 10
                sum += digit**2
                n //= 10
            if sum in end:
                return False
            else:
                end.add(sum)
            n = sum
        return True