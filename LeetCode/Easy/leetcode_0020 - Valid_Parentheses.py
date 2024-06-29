class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')', '{':'}', '[':']'}
        stack = []
        for i in s:
            if i in dic.keys():
                stack.append(i)
            else:
                if stack == [] or dic[stack.pop()] != i:
                    return False
        return stack == []
    
#Description
'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
'''

#Solution
'''
각각 대응하는 괄호들을 dictionary에 key, value로 저장함
s를 순회하며 괄호가 (, {, [ 중 하나라면 stack에 추가함
그게 아니라면 stack이 비어있거나 stack의 마지막 원소가 그것에 대응하는 괄호가 아닐 경우 False를 반황함
대응하는 괄호가 맞았을 경우 stack의 마지막 원소를 지우기위해 pop() 함수를 활용함
마지막에 stack이 비어있다면 True, 아니라면 False를 반환함
'''