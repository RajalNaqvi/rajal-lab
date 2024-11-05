"""
    Problem Statement:  
        A number is even odd special if and only if there are even digits side by side, same goes for odd digits too. 
        So the distributions must be in an alternating basis of even digits and odd digits. 
        You are given a number N, and you have to say how many special numbers are possible <=N, and are greater than 0.

    Constraints:
        1<=N<=10^8

    Input Format:
        First Line containing a single integer N.

    Output Format:
        Single line containing a single integer denoting the possible number of special numbers.

    Sample Input:
        30

    Output:
        20

    Explanation:

        20 such special numbers are there :-
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            12, 14, 16, 18,
            21, 23, 25, 27, 29, 30
    
"""


def count_special_numbers(N):
    # Convert the number to a string for easy digit-by-digit processing
    str_n = str(N)
    length = len(str_n)

    # Memoization dictionary to store the results of subproblems
    memo = {}

    # Recursive function to count special numbers
    def dp(pos, tight, prev_digit_is_odd):
        if pos == length:
            return 1

        # Memoization key based on current state
        key = (pos, tight, prev_digit_is_odd)
        if key in memo:
            return memo[key]

        # Setting the upper limit for the current digit based on the "tight" condition
        limit = int(str_n[pos]) if tight else 9

        result = 0
        for digit in range(0, limit + 1):
            # Ensure alternate parity for adjacent digits
            if (digit % 2 == 0) != prev_digit_is_odd:
                # Recurse with updated conditions
                result += dp(
                    pos + 1,
                    tight and (digit == limit),
                    digit % 2 == 1  # Check if the current digit is odd
                )

        # Store the result in memoization dictionary
        memo[key] = result
        return result

    # Start the recursion from the most significant digit
    total_special_numbers = dp(0, True, False)

    # We subtract 1 as the question requires "greater than 0"
    return total_special_numbers - 1


# Input
N = int(input())

# Output result
print(count_special_numbers(N))
