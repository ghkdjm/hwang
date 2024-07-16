N = int(input())
nums = list(map(int, input().split()))
v = int(input())
print(nums.count(v))

#Description
'''
총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.
'''
#Input
'''
첫째 줄에 정수의 개수 N(1 ≤ N ≤ 100)이 주어진다. 둘째 줄에는 정수가 공백으로 구분되어져있다. 셋째 줄에는 찾으려고 하는 정수 v가 주어진다.
입력으로 주어지는 정수와 v는 -100보다 크거나 같으며, 100보다 작거나 같다.
'''
#Output
'''
첫째 줄에 입력으로 주어진 N개의 정수 중에 v가 몇 개인지 출력한다.
'''

#Solution
'''
주어지는 숫자들을 리스트로 저장하고 count() 함수를 이용해 리스트에 v가 몇 개 있는지 출력함
*count()는 str, list, tuple에서 사용가능함
'''

#count() 함수 직접 구현
def count_direct(data, target):
    count = 0
    for i in data:
        if i == target:
            count += 1
    return count