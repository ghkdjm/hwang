N, K = map(int, input().split())
coins = list(int(input()) for A in range(N))
count = 0
for coin in coins[::-1]:
    count += K//coin
    K %= coin
print(count)

#Description
'''
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
'''
#Input
'''
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)
'''
#Output
'''
첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.
'''

#Solution
'''
동전의 가치들을 coins라는 list에 저장함
coins는 오름차순으로 정렬되어 있으므로 이를 슬라이싱을 통해 역으로 정렬한 list를 for 문을 통해 순회함
K를 coin으로 나눈 몫을 count에 더해주고 K는 coin으로 나눈 나머지로 저장함
count를 출력함
'''