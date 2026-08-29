class Solution(object):
    def removeDuplicates(self, nums):
        k=0
       
        seen=nums[0]

        for i in range(len(nums)):
            if(nums[i]!=seen):
                seen=nums[i]
                k+=1
                nums[k]=nums[i]
        return k+1