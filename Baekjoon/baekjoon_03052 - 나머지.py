nums = list(int(input()) for _ in range(10))
remainder = set()
for num in nums:
    remainder.add(num % 42)
print(len(remainder))

#Description
'''
두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 
수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.
'''
#Input
'''
첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다. 이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.
'''
#Output
'''
첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.
'''

#Solution
'''
입력받은 수 10개를 nums라는 list에 저장함
빈 set인 remainder을 정의하고
nums를 순회하며 각 수를 42로 나눈 나머지를 remainder에 추가함
set은 중복되는 원소가 없게 저장되므로 len() 함수를 이용해 remainder의 원소의 개수를 출력함
'''