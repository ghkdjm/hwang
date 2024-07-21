N, X = map(int, input().split())
A = list(map(int, input().split()))
result = []
for num in A:
    if num < X:
        result.append(num)
print(*result)

#Description
'''
정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
'''
#Input
'''
첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.
'''
#Output
'''
X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.
'''

#Solution
'''
입력한 A를 for 문을 통해 순회하며 X보다 작은 수를 result라는 빈 list에 추가함
출력 형식을 맞추기 위해 *를 이용해 출력함
* *는 두 숫자 사이에 있을 때는 곱셈 연산을 의미하고, list, tuple, set에서는 객체를 언패킹함
* dict에서 *를 사용하면 key 값들을 언패킹하고, **를 사용하면 key : value들로 언패킹됨
'''