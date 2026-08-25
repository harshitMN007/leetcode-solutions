class Solution(object):
    def missingMultiple(self, nums, k):
        nums.sort()
        NumsDiv=[]
       
       
        for i in range(len(nums)):
            if(nums[i]%k==0):
                NumsDiv.append(nums[i])
      
       

        i=1
        while(k*i in NumsDiv):
            i+=1
        return k*i

            


        