class Solution(object):
    def coinChange(self, coins, amount):
        
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        '''

        clarify exceptions/constraints:
        infinite number of each coins
        if cannot be made by any combination of coins return -1
        
        approach:
        1) sort coinslist by size
        2) loop through coins list and do floor division with coin. if cannot,
        move on to next amount. else, minus from amount. add answer to output
        3) if last element reached, any amount remaining, return -1.
        4) else return output total amount of money amount

        time/space complexity:
        
        '''

        amount_total_moneycount = 0 #initialise count of output
        coins.sort()
        for coin in coins: #loop through coinslist
            if amount // coin == 0: #amount greater than coin
                
                





s1 = Solution
s1.coinChange()
