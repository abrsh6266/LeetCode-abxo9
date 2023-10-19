class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        
        for customer_accounts in accounts:
            wealth = sum(customer_accounts)
            max_wealth = max(max_wealth, wealth)
        
        return max_wealth
