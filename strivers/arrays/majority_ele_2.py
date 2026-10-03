#brute-force

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        count={}
        ret_list=[]
        n=len(nums)

        for i in range(n):
            if(nums[i] not in count):
                count[nums[i]]=1
            else:
                count[nums[i]]+=1

        for num in count:
            if(count[num]>n//3):
                ret_list.append(num)
            
        return ret_list

        
#optimal O(1)  space and O(n) time


class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        candidate1=-(2**31)
        n=len(nums)
        count1=0
        candidate2=-(2**31)
        count2=0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1


        # Verify actual frequencies
        count1 = 0
        count2 = 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        # Return valid candidates
        if count1 > n // 3 and count2 > n // 3:
            return [candidate1, candidate2]
        elif count1 > n // 3:
            return [candidate1]
        elif count2 > n // 3:
            return [candidate2]
        else:
            return []
        
            




            


        
            



            


        



        