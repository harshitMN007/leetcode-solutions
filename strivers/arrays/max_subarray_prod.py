//brute force approach 
import numpy as np
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maximum=-(2**32)

        for i in range(len(nums)):
            prod=1
            for j in range(i,len(nums)):
                prod*=nums[j]
                maximum=max(prod,maximum)
        return maximum
        
        
//optimised approach prefix and suffix

import numpy as np
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        prefix=1
        suffix=1
        ans=float('-inf')

        for i in range(len(nums)):
            if(prefix==0):
                prefix=1
            if(suffix==0):
                suffix=1
            
            prefix*=nums[i]
            suffix*=nums[len(nums)-1-i]

            ans=max(ans,max(prefix,suffix))

        return ans

//kadane approach whether to extend or start new subarray
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        ans = nums[0]

        for num in nums[1:]:
            if num < 0:
                cur_max, cur_min = cur_min, cur_max

            cur_max = max(num, cur_max * num)
            cur_min = min(num, cur_min * num)

            ans = max(ans, cur_max)

        return ans

            

