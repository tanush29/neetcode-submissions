class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for i, num in enumerate(nums):
            if num in num_dict:
                return True
            else:
                num_dict[num] = i
        return False