
"""
Problem 002: Best Time to Buy and Sell Stock
Platform: LeetCode
Difficulty: Easy
Topic: Array

Time Complexity: O(n)
Space Complexity: O(1)
"""

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price

        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(max_profit(prices))
