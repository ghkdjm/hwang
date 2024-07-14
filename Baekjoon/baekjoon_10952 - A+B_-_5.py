while True:
    A, B = map(int,input().split())
    if A == B == 0:
        break
    print(A + B)

#Description
'''
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
'''
#Input
'''
입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
입력의 마지막에는 0 두 개가 들어온다.
'''
#Output
'''
각 테스트 케이스마다 A+B를 출력한다.
'''

#Solution
'''
while 문을 사용하여 A, B를 입력받고 A, B가 둘 다 0이 아닌 경우에는 A+B를 출력함
A, B가 둘 다 0이면 break를 통해 while 문을 중단함
'''