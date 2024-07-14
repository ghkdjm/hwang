for i in range(1, (N := int(input()))+1):
    print('*' * i)

#Description
'''
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
'''
#Input
'''
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
'''
#Output
'''
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
'''

#Solution
'''
첫째 줄부터 N번째 줄 까지 각각 1개부터 N개까지 *이 출력되므로 범위를 range(1, N+1)로 설정함
i번째 줄에 '*'를 i개 출력함
'''