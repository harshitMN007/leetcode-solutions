class Solution(object):
    def majorityElement(self, nums):
        count={}
        maximum=0
        
        for i in nums:
            if(i not in count):
                count[i]=1
            else:
                count[i]+=1

        for i in count:
            if(count[i]>maximum):
                if(count[i]>(len(nums)/2)):
                    maximum=i
        return maximum
        
        
    #effiecint way below
    
    class Solution(object):
    def majorityElement(self, nums):
        candidate = 0
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate