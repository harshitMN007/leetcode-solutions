//using an extra space
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        temp=0
        seen={}
 
        for i,num in enumerate(numbers):
            temp=target-num

            if temp in seen:
                return [seen[temp],i+1]
            
            seen[num]=i+1
            

#if we need to use a constant space approach we use the two pointer method            
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left=0;right=len(numbers)-1
        
        while(left<right):
            total=numbers[left]+numbers[right]
            
            if(total==target):
                return [left+1,right+1]
            elif(total>target):
                right-=1
            else:
                left+=1
                

            



                    




        