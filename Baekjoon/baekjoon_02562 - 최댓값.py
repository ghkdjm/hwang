nums = list(int(input()) for _ in range(9))
print(max(nums))
print(nums.index(max(nums)) + 1)

#Description
'''
9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
예를 들어, 서로 다른 9개의 자연수 3, 29, 38, 12, 57, 74, 40, 85, 61 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.
'''
#Input
'''
첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.
'''
#Output
'''
첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.
'''

#Solution
'''
9개의 수를 nums라는 list로 저장함
max() 함수를 사용해 최댓값을 구하고 index() 메소드를 통해 그 값이 몇 번째 수인지 알아냄
index는 0부터 시작하므로 1을 더해서 출력해야함
'''

#dict 이용
index = 1
nums = dict()
while index <= 9:
    nums[int(input())] = index
    index += 1
print(max(nums))
print(nums[max(nums)])
'''
입력하는 숫자를 key 값으로 하고 그게 몇 번째 입력인지를 value 값으로 하여 nums라는 dict로 저장함
max() 함수를 사용해 nums의 key 값들 중 가장 큰 값을 출력하고 그 값의 value 값을 출력함
* dict에서 max() 함수를 사용하면 key 값들 중 가장 큰 값을 반환함(아스키코드 순서)
'''