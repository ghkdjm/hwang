N = int(input())
for i in range(N//5, -1, -1):
    remain = N - (5 * i)
    if remain % 3 == 0:
        print(remain//3 + i)
        break
else: print(-1)

#Description
'''
상근이는 요즘 설탕공장에서 설탕을 배달하고 있다.상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다.
설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다.
예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.
상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.
'''
#Input
'''
첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)
'''
#Output
'''
상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.
'''

#Solution
'''
3보다 5가 더 크므로 5kg 설탕 봉지가 더 많을수록 더 적은 개수의 봉지를 배달할 수 있음
범위를 range(N//5, -1, -1)로 설정해 N을 5로 나눈 몫부터 역으로 0까지 반복하도록 함
이때 N에서 5*i를 뺀 나머지가 3으로 나누어 떨어지면 그 나머지를 3으로 나눈 몫과 i를 더한 값을 출력함
반복문이 종료될 때까지 나누어 떨어지는 경우가 없으면 -1을 출력함
'''

#함수를 이용한 답
def solution(N):
    for i in range(N//5, -1, -1):
        remain = N - (5 * i)
        if remain % 3 == 0:
            return remain//3 + i
    return -1

print(solution(N := int(input())))

#3x + 5y = N의 모든 해를 비교해 구한 답
N = int(input())
solutions = []
for x in range(N//3 + 1):
    for y in range(N//5 + 1):
        if 3*x + 5*y == N:
            solutions.append(x + y)
if solutions:
    print(min(solutions))
else:
    print(-1)