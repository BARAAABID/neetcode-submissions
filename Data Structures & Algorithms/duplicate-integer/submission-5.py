class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if 0 <= len(nums) and len(nums) <= 10**5:
            seen = set()
            for i in range (len(nums)):
                if nums[i] in seen:
                    return True
                seen.add(nums[i])
            return False
        else:
            return False