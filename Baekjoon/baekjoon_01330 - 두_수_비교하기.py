A, B = map(int, input().split())
if A > B: print('>')
elif A < B: print('<')
else: print('==')

#Description
'''
두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
'''
#Input
'''
첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.
'''
#Output
'''
첫째 줄에 다음 세 가지 중 하나를 출력한다.
 - A가 B보다 큰 경우에는 '>'를 출력한다.
 - A가 B보다 작은 경우에는 '<'를 출력한다.
 - A와 B가 같은 경우에는 '=='를 출력한다.
'''

#Solution
'''
if-elif-else 문을 이용해 문제 조건에 맞춰 입출력을 함
'''