class Solution(object):
    def removeDuplicates(self, nums):
        seen=nums[0]
        count=0
        track=0
        k=1

        for i in range(len(nums)):
            if(nums[i]==seen and count<2):
                count+=1
                nums[track]=nums[i]
                track+=1
            else:
                if(nums[i]!=seen):
                    count=1
                    seen=nums[i]
                    nums[track]=nums[i]
                    track+=1
                    k+=1
        return track
                   
                
                
               
                









        