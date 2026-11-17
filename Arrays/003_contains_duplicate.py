
"""
Problem 003: Contains Duplicate
Platform: LeetCode
Difficulty: Easy
Topic: Array, Set, Hashing

Time Complexity: O(n) average
Space Complexity: O(n)
"""

def contains_duplicate(nums):
    return len(nums) != len(set(nums))


if __name__ == "__main__":
    nums = [1, 2, 3, 1]

    print(contains_duplicate(nums))
