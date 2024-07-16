dice = list(map(int, input().split()))
counts = {}
for die in dice:
    if die in counts: counts[die] += 1
    else: counts[die] = 1
if len(counts) == 3: 
    print(max(dice) * 100)
else:
    for die, count in counts.items():
        if count == 3:
            print(10000 + die * 1000)
            break
        elif count == 2:
            print(1000 + die * 100)
            break

#Description
'''
1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.
 1. 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
 2. 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
 3. 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3×100으로 계산되어 1,300원을 받게 된다.
또 3개의 눈이 2, 2, 2로 주어지면 10,000+2×1,000 으로 계산되어 12,000원을 받게 된다.
3개의 눈이 6, 2, 5로 주어지면 그중 가장 큰 값이 6이므로 6×100으로 계산되어 600원을 상금으로 받게 된다.
3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성 하시오.
'''
#Input
'''
첫째 줄에 3개의 눈이 빈칸을 사이에 두고 각각 주어진다.
'''
#Output
'''
첫째 줄에 게임의 상금을 출력한다.
'''

#Solution
'''
dice를 순회하며 각 숫자가 얼마나 나왔는지 counts에 저장함
len(counts)가 3이면 max(dice) * 100을 출력함
아니면 counts를 순회하며 items() 함수를 사용해 counts의 각 key 값과 value 값을 tuple로 저장하고
value 값이 3이면 10000 + 해당 key 값 * 1000을 출력하고
value 값이 2이면 1000 + 해당 key 값 * 100을 출력함
'''

#묶인 데이터 타입을 사용하지 않은 답
a, b, c = map(int, input().split())
if a == b == c:
	print(10000 + a * 1000)
elif a == b or a == c or b == c:
	if a == b or a == c:
		print(1000 + a * 100)
	else:
        print(1000 + b *100)
else:
    print(max(a, b, c) * 100)
