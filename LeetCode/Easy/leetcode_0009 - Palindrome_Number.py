class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x[::-1] == x

#Description
'''
Given an integer x, return true if x is a palindrome, and false otherwise.
'''

#Solution
'''
int형 자료를 str형 자료로 변환한 후 슬라이싱을 통해 x를 거꾸로 배열한 것과 x를 비교함
같으면 True, 다르면 False를 반환함
'''

#int형 자료형을 str형 자료형으로 바꾸지 않고 하는 방법
class Solution:
    def isPalindrome(x: int) -> bool:
        num = []
        while x:
            num.append(x % 10)
            x //= 10
        return num == reversed(num)
