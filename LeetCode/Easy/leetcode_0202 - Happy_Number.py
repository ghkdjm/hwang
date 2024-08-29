class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            sum = 0
            while n > 0:
                digit = n % 10
                sum += digit**2
                n //= 10
            if sum in seen:
                return False
            else:
                seen.add(sum)
            n = sum
        return True

#Description
'''
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
 - Starting with any positive integer, replace the number by the sum of the squares of its digits.
 - Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
 - Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
'''

#Solution
'''
주어진 n에 대하여 주어진 계산을 진행하다보면 Happy Number가 아닌 경우에는 항상 똑같은 수가 반복되어 나옴
이미 계산되어 나온 수를 seen에 추가하고 계속 계산을 하다가 seen에 그 수가 존재한다면 False를 반환함
그렇지 않으면 True를 반환함
'''
