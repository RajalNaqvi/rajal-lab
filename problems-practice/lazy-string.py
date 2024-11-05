"""Problem Statement-:  
    Anish is the laziest person you can ever see. 
    He is tasked to write the name of the winner in a game where two people take part. 
    And he just writes the longest common subsequence over there, so that with minimum chane or no backspace he can edit the name to the winner’s name.

    For two given names, you have to predict what Anish will write in his computer before the start of the name. 
    If there are more than two longest subsequences possible,write the one with less lexicographic value.


    Input Format:
        Two lines including two strings of name(All with capital letters)
    
    Output Format:
        A single line with the lexicographically smallest possible longest common subsequence.
    
    Sample Input:
        ABCD
        BACD

    Sample Output:
        ACD

    Explanation:
        ACD and BCD these are the two possible biggest substring
"""


def longest_common_subsequence(s1, s2):
    len1, len2 = len(s1), len(s2)
    # Initialize DP table for lengths of LCS

    dp = [["" for _ in range(len2 + 1)] for _ in range(len1 + 1)]
    
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            
            if s1[i - 1] == s2[j - 1]:
                # If characters match, add to LCS
                dp[i][j] = dp[i - 1][j - 1] + s1[i - 1]
            else:
                # Take the longer subsequence; if equal, take lexicographically smaller
                if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                    dp[i][j] = dp[i - 1][j]
                elif len(dp[i - 1][j]) < len(dp[i][j - 1]):
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1])
    # The result is the LCS with lexicographic order guaranteed
    return dp[len1][len2]

s1 = input().strip()
s2 = input().strip()

# Output the lexicographically smallest LCS
print(longest_common_subsequence(s1, s2))
