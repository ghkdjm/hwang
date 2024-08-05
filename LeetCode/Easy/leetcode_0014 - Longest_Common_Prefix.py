class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        first_str, last_str = strs[0], strs[-1]
        result = ''
        for i in range(len(first_str)):
            if i < len(last_str) and first_str[i] == last_str[i]:
                result += first_str[i]
            else: break
        return result

#Description
'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''
#문제 해석
'''
strs의 str들이 공통으로 가지고있는 가장 긴 접두사를 찾아야 함
'''

#Solution
'''
str으로 구성된 list를 sorted를 통해 배열하면 사전 순(아스키코드 순)으로 배열됨
정렬된 strs의 첫 원소와 마지막 원소만 비교하면 답을 구할 수 있음
first_str과 last_str을 앞에서부터 한 글자씩 비교하여 두 문자가 같으면 result에 추가하고 다르면 break하여 result를 반환함
'''
