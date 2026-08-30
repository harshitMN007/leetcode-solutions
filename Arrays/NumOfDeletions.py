class Solution(object):
    def minimumDeletions(self, nums):
        n = len(nums)

        max_index = nums.index(max(nums))
        min_index = nums.index(min(nums))

        option1 = max(max_index, min_index) + 1

        option2 = n - min(max_index, min_index)

        option3 = min_index + 1 + (n - max_index)

        option4 = max_index + 1 + (n - min_index)

        return min(option1, option2, option3, option4)


