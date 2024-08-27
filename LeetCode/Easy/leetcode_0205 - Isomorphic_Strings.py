class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st, ts = {}, {}
        for char_s, char_t in zip(s, t):
            if char_s in st and st[char_s] != char_t:
                return False
            else:
                st[char_s] = char_t
            if char_t in ts and ts[char_t] != char_s:
                return False
            else:
                ts[char_t] = char_s
        return True
    
#Description
'''
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.
'''

#Solution
'''
st와 ts라는 dict를 만듦
s의 각 글자를 t의 각 글자와 비교하여 다른 것이 있다면 False를 반환함
t의 각 글자를 s의 각 글자와 비교하여 다른 것이 있다면 False를 반환함
한 방향만 비교한다면 단어가 모두 다른 글자로 구성된 경우 항상 True를 반환하기에 양 방향을 모두 비교해야함
'''