class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)
        left = 0
        while left < n:
            right = left + 1
            while right<n and prices[right]>= prices[left]:
                max_profit= max(max_profit, (prices[right]-prices[left]))
                right+=1
            left+=1
        return max_profit
        