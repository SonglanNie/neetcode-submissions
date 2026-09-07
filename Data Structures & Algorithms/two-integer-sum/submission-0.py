class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}

        for i in range(len(nums)):
            i_val = nums[i]
            j_val = target - i_val
            j = idx.get(j_val, -1)
            if j == -1:
                idx[i_val] = i
            else:
                return [j,i]
