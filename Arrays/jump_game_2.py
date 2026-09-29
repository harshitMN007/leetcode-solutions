//method-1
class Solution:
    def jump(self, nums: list[int]) -> int:
        goal=len(nums)-1
       
        count=0

        while(goal!=0):
            for i in range(goal):
                if(i+nums[i]>=goal):
                    count+=1
                    goal=i
                    break
        return count

 //method-2
 class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == end:
                jumps += 1
                end = farthest

        return jumps