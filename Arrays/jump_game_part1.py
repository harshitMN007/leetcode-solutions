class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal=len(nums)-1

        def req(goal):
            if goal==0:
                return True
            else:
            
                for i in range(goal-1,-1,-1):
                    if(i+nums[i]>=goal):
                        goal=i
                        return req(goal)

                return False
                
        return req(goal)    
        
        
  #method-2      
 class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0
