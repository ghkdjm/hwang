class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1, 'V':5, 'X': 10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        for i in range(len(s)-1):
            if dic[s[i]] < dic[s[i+1]]:
                result -= dic[s[i]]
            else:
                result += dic[s[i]]
        result += dic[s[-1]]
        return result
    
#Description
'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
 - I can be placed before V (5) and X (10) to make 4 and 9. 
 - X can be placed before L (50) and C (100) to make 40 and 90. 
 - C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
'''

#Solution
'''
주어진 조건에 맞게 로마 숫자와 정수 값을 매핑한 것을 dict로 만듦
주어진 str인 s를 마지막 문자를 제외하고 for 문을 통해 순회함
이때, 그 로마 숫자의 값이 그 다음 순서의 로마 숫자 값보다 작으면 해당 로마숫자의 값만큼을 빼줌
즉, IV 또는 IX인 경우에는 1을, XL 또는 XC인 경우에는 10을, CD 또는 CM인 경우에는 100을 빼줌
마지막 로마 숫자의 값을 더해준 결과을 반환함
'''