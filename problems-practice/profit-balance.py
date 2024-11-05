"""
    Problem Statement-: 
    Anand and Brijesh got a bunch of profit in their business. Now it’s time to divide the profit between themselves.
    Anand being the one with the calculator was the one who could decide who will get how much.
    But as he was one hell of an honest guy, he can’t cheat on Brijesh to get some extra money. 
    So he decided to divide them in such a way where they can get almost the same amount possible. 
    Although, it is sometimes impossible to divide the profit into two, because the profits must be written in their production managed copy in a way where you cannot share the profit of a single thing, 
    A single Profit will be held by a single person.

    You are the one who is called to mitigate the problem. Given an array of profit, find out in the process, what can be the minimum difference between them in terms of income.

    

    Constraints:
    1<=N<=10^3
    0<=Profits<=1000
    
    Input Format:
        First line contains an integer N, number of profits.
        Next line, N space separated Integers denoting the i-th Profit.
    

    Output:
        A single integer denoting minimum possible difference between the total profits.
    

    Sample Input:
        4
        1 2 3 4

    Output:
        0

    Explanation:
        He will take 1 and 4, so his profit will be 5, so the difference will be 0.
"""

def min_difference_partition(profits):
    n = len(profits)
    total_sum = sum(profits)

    # Initialize DP table
    # dp[i][j] will be True if a subset with sum j can be formed using the first i elements.
    dp = [[False] * (total_sum + 1) for _ in range(n + 1)]
    dp[0][0] = True

    # Populate the DP table
    for i in range(1, n + 1):
        for j in range(total_sum + 1):
            # If the subset sum j can be formed without the current element
            dp[i][j] = dp[i - 1][j]

            # If the subset sum j can be formed with the current element
            if j >= profits[i - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j - profits[i - 1]]

    # Find the minimum difference by exploring achievable subset sums
    min_diff = float('inf')
    for j in range(total_sum // 2 + 1):
        if dp[n][j]:
            min_diff = min(min_diff, total_sum - 2 * j)

    return min_diff


# Input handling
n = int(input())
profits = list(map(int, input().split()))

# Output result
print(min_difference_partition(profits))
