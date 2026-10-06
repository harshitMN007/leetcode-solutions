//better approach

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        unique_triplets=set()

        for i in range(len(nums)-2):
            seen=set()
            for j in range(i+1,len(nums)):
                third=-(nums[i]+nums[j])
                if third in seen:
                    triplet = tuple(sorted((nums[i], nums[j], third)))
                    unique_triplets.add(triplet)
                else:
                    seen.add(nums[j])


        return [list(trip) for trip in unique_triplets]


            
            


 //optimal solution
 
 class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        numbers=[]
        nums.sort()
        n=len(nums)

        for i in range(len(nums)):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            j=i+1
            k=n-1

            while(j<k):
                total=nums[i]+nums[j]+nums[k]

                if(total<0):
                    j+=1
                elif(total>0):
                    k-=1
                else:
                    numbers.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while(j<k and nums[j]==nums[j-1]):
                        j+=1
        return numbers