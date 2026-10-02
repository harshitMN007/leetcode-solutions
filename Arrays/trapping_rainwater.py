//bruteforce approach-time limit exceeds

class Solution:
    def trap(self, height: list[int]) -> int:
        rainwater=0

        for i in range(len(height)):
            lmax=0
            rmax=0

            for j in range(i+1):
                lmax=max(lmax,height[j])

            for k in range(i,len(height)):
                rmax=max(rmax,height[k])
            
            rainwater+=min(lmax,rmax)-height[i]



                
        return rainwater       
        
//best solution

class Solution:
    def trap(self, height: list[int]) -> int:
        lmax=[0]*len(height)
        rmax=[0]*len(height)
        lmax[0]=height[0]
        rainwater=0
        for i in range(1,len(height)):
            lmax[i]=max(lmax[i-1],height[i])
        rmax[len(height)-1]=height[len(height)-1]
        for i in range(len(height)-2,-1,-1):
            rmax[i]=max(rmax[i+1],height[i])

        for i in range(len(height)):
            rainwater+=min(lmax[i],rmax[i])-height[i]

        return rainwater

//optimal solution

class Solution:
    def trap(self, height: list[int]) -> int:
        lmax=0;rmax=0
        n=len(height)
        rainwater=0
        left=0
        right=n-1

        while(left<right):
            lmax=max(lmax,height[left])
            rmax=max(rmax,height[right])

            if(lmax<rmax):
                rainwater+=lmax-height[left]
                left+=1
            else:
                rainwater+=rmax-height[right]
                right-=1
        return rainwater




            
            



        