//brute force approach

class Solution(object):
    def hIndex(self, citations):
    
        maximum=max(citations)
        hindex=0
        

        for i in range(1,maximum+1):
            h=i
            count=0
            for j in range(len(citations)):
                if(citations[j]>=h):
                    count=count+1
            if(count>=h):
                if(h>hindex):
                    hindex=h
        return hindex
                


#time=O(len*max(citations))
#space=O(1)

class Solution(object):
    def hIndex(self, citations):
        citations.sort()
  
        for i in range(len(citations)):
            h=len(citations)-i
            
            if(citations[i]>=h):
                return h
                
#time=O(len*log len)
#space=O(1)
            
            

