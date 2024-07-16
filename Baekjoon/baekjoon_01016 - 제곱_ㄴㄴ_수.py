m, M = map(int, input().split())
lst = [1] * (M - m + 1)
i = 2
while i**2 <= M:
    start = max(i**2, (m + i**2 - 1)//(i**2) * (i**2))
    for j in range(start, M+1, i**2):
        lst[j - m] = 0
    i += 1
count = sum(lst)
print(count)

#Description
'''
어떤 정수 X가 1보다 큰 제곱수로 나누어 떨어지지 않을 때, 그 수를 제곱ㄴㄴ수라고 한다. 제곱수는 정수의 제곱이다.
min과 max가 주어지면, min보다 크거나 같고, max보다 작거나 같은 제곱ㄴㄴ수가 몇 개 있는지 출력한다.
'''
#Input
'''
첫째 줄에 두 정수 min과 max가 주어진다.
'''
#Output
'''
첫째 줄에 min보다 크거나 같고, max보다 작거나 같은 제곱ㄴㄴ수의 개수를 출력한다.
'''

#Solution
'''
(M - n + 1)개의 1로 구성된 lst를 만듦
lst에서 제곱수의 배수들에 해당하는 index의 수를 0으로 바꿈
단순히 제곱수의 배수만큼 수를 빼준다면 중복되는 수는 여러번 빠지므로 list를 이용하여 계산하는 것이 더 정확함
start는 m과 M 사이의 가장 작은 제곱수의 배수이다
'''
