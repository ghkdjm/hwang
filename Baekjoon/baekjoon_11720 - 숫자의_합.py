N = int(input())
nums = input()
print(sum(int(num) for num in nums))

#Description
'''
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
'''
#Input
'''
첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.
'''
#Output
'''
입력으로 주어진 숫자 N개의 합을 출력한다.
'''

#Solution
'''
리스트 내포(list comprehension)를 통해 입력받은 str의 각 문자를 정수로 변환하고 sum() 함수를 사용하여 합을 구함
'''