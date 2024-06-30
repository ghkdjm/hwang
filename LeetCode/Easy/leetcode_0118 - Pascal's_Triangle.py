class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        def pascal(lst):
            row = [1]
            for i in range(len(lst)-1):
                row.append(lst[i] + lst[i+1])
            row.append(1)
            return row
        result = [[1]]
        for i in range(numRows-1):
            result.append(next(result[i]))
        return result
    
#Description
'''
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it
'''

#Solution
'''
파스칼의 삼각형에서 한 행이 주어졌을 때 다음 행을 구하여 반환하는 함수를 정의함
주어진 행의 두 항의 합을 순서대로 1이 하나 들어있는 list에 추가하고 마지막에 또 1을 추가함
[[1]]이라는 리스트를 만들고 주어진 numRows만큼 정의한 함수를 통해 얻은 list를 [[1]]에 추가함
'''
