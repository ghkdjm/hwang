class Solution:
    def sortColors(self, nums: list[int]) -> None:
        counts = [0, 0, 0]
        for num in nums:
            counts[num] += 1
        r, w, b = counts[0], counts[1], counts[2]
        for i in range(r):
            nums[i] = 0
        for j in range(w):
            nums[r + j] = 1
        for k in range(b):
            nums[r + w + k] = 2
        return nums
    
#Description
'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.
'''
#문제 해석
'''
0, 1, 2로 구성된 nums를 sort 함수를 사용하지 않고 list 내부에서 수를 정렬하기
'''

#Solution
'''
nums에는 0, 1, 2만 존재하므로 counts라는 list를 만들어 nums의 각 수가 counts의 index가 됨
이를 활용해 nums에 0, 1, 2가 각각 몇 개 있는지 개수를 셀 수 있음
nums의 각 원소를 0, 1, 2의 개수만큼 0, 1, 2로 순서대로 바꾼 후 nums를 반환함
'''
