class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        def pascal(lst):
            row = [1]
            for i in range(len(lst) - 1):
                row.append(lst[i] + lst[i + 1])
            row.append(1)
            return row
        result = [1]
        for i in range(rowIndex):
            result = pascal(result)
        return result
    
#Description
'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it
'''

#Solution
'''
파스칼의 삼각형에서 한 행이 주어졌을 때 다음 행을 구하여 반환하는 함수를 정의함
주어진 list의 두 항의 합(lst[i] + lst[i + 1])을 순서대로 [1]에 추가하고 마지막에 또 1을 추가함
result를 [1]로 정의하고 주어진 rowIndex만큼 정의한 함수를 통해 얻은 list를 result로 재정의하여 반환함
'''
