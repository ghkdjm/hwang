class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x[::-1] == x:
            return True
        return False

#Description
#Given an integer x, return true if x is a palindrome, and false otherwise.

#Solution
#int형 자료를 str형 자료로 변환한 후 슬라이싱을 통해 x를 거꾸로 배열한 것과 x를 비교함
#같으면 True, 다르면 False를 반환함
