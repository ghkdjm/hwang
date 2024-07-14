result = 0
for i in range(1, (n := int(input()))+1):
    result += i
print(result)

#Description
'''
n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
'''
#Input
'''
첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.
'''
#Output
'''
1부터 n까지 합을 출력한다.
'''

#Solution
'''
for 문을 사용하여 0에 1부터 n까지 더한 후 그 값을 출력함
이외에도 이를 구현할 수 있는 방법이 있음
'''

#while 문 사용
'''
n = int(input())
result = 0
while n:
    result += n
    n -= 1
print(result)
'''

#1부터 n까지의 합 공식 사용
'''
n = int(input())
print((n * (n+1))//2)
'''

#sum 함수 사용
'''
print(sum(range(1, (n := int(input()))+1)))
'''

#재귀 함수 사용
'''
def sum_recursive(n):
    if n == 1:
        return 1
    else: return n + sum_recursive(n-1)

print(sum_recursive(n := int(input())))
'''