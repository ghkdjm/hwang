class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {1000:'M',500:'D',100:'C',50:'L',10:'X',5:'V',1:'I',0:''}
        i = 1000
        result = ''
        while i:
            digit = num//i
            if digit == 4 or digit == 9:
                result += dic[i] + dic[(digit + 1)*i]
            else: result += dic[(digit//5)*5*i] + dic[i] * (digit % 5)
            num %= i
            i //= 10
        return result
    
#Description
#Seven different symbols represent Roman numerals with the following values: 
#{1000:'M', 500:'D', 100:'C', 50:'L', 10:'X', 5:'V', 1:'I'}
#Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:
#If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
#If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 
#{4:'IV', 9:'IX', 40:'XL', 90:'XC', 400:'CD', 900:'CM'}
#Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
#Given an integer, convert it to a Roman numeral.

#Solution
#주어진 조건에 맞게 dictionary를 생성하고, {0:''}도 추가한다
#1000의 자리부터 100, 10, 1의자리 순으로 계산한다
#그 자리 수가 4 또는 9이면 dic[i] + dic[(digit + 1)*i]를 추가하도록 한다
#나머지 경우에는 5 이상일 때를 고려하여 dic[(digit//5)*5*i] + dic[i] * (digit % 5)를 추가한다
