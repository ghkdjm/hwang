for i in range(1, (T := int(input()))+1):
    A, B = map(int, input().split())
    print(f"Case #{i}: {A + B}")

#Description
'''
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
'''
#Input
'''
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
'''
#Output
'''
각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.
'''

#Solution
'''
케이스 번호가 1부터 T까지 되야하므로 range(1, T+1)로 범위를 설정하여 "Case #x: "를 출력하고 A+B를 출력함
출력에서 f-string을 사용하여 출력함
'''