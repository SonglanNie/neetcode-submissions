class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in idx:
                return [idx[diff], i]
            else:
                idx[num] = i

                