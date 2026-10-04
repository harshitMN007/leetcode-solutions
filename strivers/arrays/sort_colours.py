class Solution:
    
    def sortColors(self, nums: list[int]) -> None:
        zeroes=0
        ones=0
        twos=0
        index=0
        

        for num in nums:
            if(num==0):
                zeroes+=1
            elif(num==1):
                ones+=1
            elif(num==2):
                twos+=1
        
        def sort(num,count):
            nonlocal index
            
            for i in range(count):
                nums[index]=num
                if(index!=len(nums)-1):
                    index+=1

        
        sort(0,zeroes)
        sort(1,ones)    
        sort(2,twos)










        