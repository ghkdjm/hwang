class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            a = target - nums[i]
            if a in nums:
                if nums.index(a) != i:
                    return [i, nums.index(a)]

#Description
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''

#Solution
'''
nums를 1번 순회하며 합이 target이 되는 두 수의 index를 찾아 반환함
target - nums[i]가 nums에 있어도 그 수가 nums[i]와 같은 수일 수 있으므로 6번째 줄의 조건도 필요함
ex)target = 6, nums = [3, 2, 4] --> 3 + 3 = 6
'''

#정수값:인덱스로 dict를 만들어 답 구하는 방법
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val not in dic: dic[nums[i]] = i
            else: return [i, dic[val]]
