class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            a = target - nums[i]
            if a in nums:
                if nums.index(a) != i:
                    return [i, nums.index(a)]

#Description
#Given an integer x, return true if x is a palindrome, and false otherwise.

#nums를 1번 순회하며 합이 target이 되는 두 수의 index를 찾음
