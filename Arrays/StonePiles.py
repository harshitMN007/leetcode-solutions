# /*
# class Solution(object):
    # def stoneGame(self, piles):
        # alice=0
        # bob=0
        # temp=True
        # sum1=0
        # sum2=0

        # while(temp):
            # if(len(piles)>=4):
                # sum1==piles[0]+piles[2]
                # sum2=piles[-1]+piles[-3]
            # else:
                # sum1=piles[0]
                # sum2=piles[-1]

            # if(sum1>sum2):
                # alice+=piles[0]
                # piles.pop(0)
            
            # else:
                # alice+=piles[-1]
                # piles.pop(len(piles)-1)

            
            # if(len(piles)>=5):
                # sum1=piles[0]
                # sum2=piles[-1]

                # if(piles[1]>piles[-2]):
                    # bob+=sum2
                    # piles.pop(-1)
                # else:
                    # bob+=sum1
                    # piles.pop(0)


            # else:                
                # sum1=piles[0]
                # sum2=piles[-1]

                # if(sum1>sum2):
                    # bob+=sum1
                    # piles.pop(0)
                # else:
                    # bob+=sum2
                    # piles.pop(-1)


            # # if(sum1>sum2):
            # #     bob+=piles[0]
            # #     piles.pop(0)
            
            # # else:
            # #     bob+=piles[-1]
            # #     piles.pop(len(piles)-1)

            # if(len(piles)==0):
                # temp=False

        # return alice>bob
# */
            
 class Solution(object):
    def stoneGame(self, piles):
        length=len(piles)
        sum_even=0
        
        sum_odd=0
        alice=0
        bob=0

        for i in range(length):
            if(i%2==0):
                sum_even+=piles[i]

            else:
                sum_odd+=piles[i]

        alice=sum_even if sum_even>sum_odd else sum_odd

        return True

        
     #or still the code can be shottened to 
    class Solution(object):
        def stoneGame(self, piles)
            return True #as alice always wins(odd or even parity)
     
     
     
     
