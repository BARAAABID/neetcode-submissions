class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest_seq = 0

        # Check if left nieghbor exists
        # Check if it is a start of a seq
        for num in nums:
            if (num - 1) not in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1
                longest_seq = max(length, longest_seq)
        return longest_seq
