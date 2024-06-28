class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            a = target - nums[i]
            if a in nums:
                if nums.index(a) != i:
                    return [i, nums.index(a)]

#Description
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

#Solution
#nums를 1번 순회하며 합이 target이 되는 두 수의 index를 찾아 반환함
