import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        additional=[]
        for i in range(len(nums)):
            curr=i
            j=i
            suffix=math.prod(nums[j+1::]) if curr!=(len(nums)-1) else 1
            prefix=math.prod(nums[0:j]) if curr != 0 else 1
            prod=suffix * prefix

            additional.append(prod)
        return additional


# the above consumes a time of O(n^2)

import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=1
        suffix=1
        additional=[0]*len(nums)
        
        for i in range(len(nums)):
            additional[i]=prefix
            prefix*=nums[i]
            
        for i in range(len(nums)-1,-1,-1):
            additional[i]*=suffix
            suffix*=nums[i]
            
        return additional
            
