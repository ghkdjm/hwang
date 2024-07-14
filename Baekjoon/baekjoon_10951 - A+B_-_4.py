while True:
    try:
        A, B = map(int,input().split())
        print(A+B)
    except:
        break

#Description
'''
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
'''
#Input
'''
입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
'''
#Output
'''
각 테스트 케이스마다 A+B를 출력한다.
'''
#문제 해석
'''
A, B를 입력받고 A+B를 출력하고, error가 발생하면 중단함
'''

#Solution
'''
while 문을 사용하여 반복해서 A, B를 입력받고 A+B를 출력함
try - except 문을 사용하여 error가 발생하면 break를 통해 while 문을 중단함
'''