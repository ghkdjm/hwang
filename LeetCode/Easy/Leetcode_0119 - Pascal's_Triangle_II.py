class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        def pascal(lst):
            result = [1]
            for i in range(len(lst) - 1):
                result.append(lst[i+1] + lst[i])
            result.append(1)
            return result
        result = [[1]]
        for i in range(rowIndex + 1):
            result.append(pascal(result[i]))
        return result[rowIndex]