class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        cnt = {}
        for num in nums:
            if num in cnt:
                cnt[num] += 1
            else:
                cnt[num] = 1
            if cnt[num] > n//2:
                return num
            
#Description
'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
'''

#Solution
'''
hash라는 dict를 만들고 nums를 순회하며 각 num들의 개수를 hash에 저장함
그 개수가 n//2보다 많으면 수 num을 반환함
'''
