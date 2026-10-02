//method-1 and also time-O(n) and space O(1)
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left=0 
        right=len(height)-1
        area=min(height[left],height[right])*(right-left)

        


        while((right-left)!=1):
            def AREA(left,right):
                
                return min(height[left],height[right])*(right-left)

            if(height[left]<=height[right]):
                left+=1
                if(AREA(left,right)>area):
                    area=AREA(left,right)
            elif(height[right]<height[left]):
                right-=1
                if(AREA(left,right)>area):
                    area=AREA(left,right)     

        return area          
        
 //method-2 a little improvemnt no change in time and the space comlexity
 
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0

        while left < right:
            curr_area = min(height[left], height[right]) * (right - left)
            area = max(area, curr_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return area

