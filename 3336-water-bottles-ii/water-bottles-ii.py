class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        x=numBottles

        while numBottles>=numExchange:
            numBottles -=numExchange-1
            numExchange+=1
            x+=1
            # print(numBottles,numExchange,c)

        return x      