"""Problem Statement-: 
        After JEE Mains, some students got admission into an engineering college. 
        Now there is a class consisting of such n students, and the HOD came to say it is time to select the class monitor. 
        But He never gets all of them at one time. So he brought a register, every time he gets someone with less rank than the previous time he cut the name and wrote the name of the student and the rank.

        name_cuts= ?
        no_of_students = 6
        if rank < previous:
            name_cuts off


    For a given number of ranks he gets each time, you have to predict how many names are cut in the list.

    Constraints:
        Number of Visiting<=10^9
        ranks <=10000
    

    Input Format:
        Number of Visiting N in their first line
        N space separated ranks the HOD gets each time
    

    Output Format:
        Number of ranks cut in the list
    

    Sample Input:
        6
        4 3 7 2 6 1


    Sample Output:
        3
    """
    
    
    
def count_rank_cuts(ranks):
    # Initialize stack and cuts counter
    stack = []
    cuts = 0

    for rank in ranks:
        while stack and stack[-1] > rank:
            cuts += 1
            stack.pop()
        if stack:
            stack.pop()
        stack.append(rank)

    return cuts

# Input
n = int(input())
ranks = list(map(int, input().split()))

# Output the result
print(count_rank_cuts(ranks))
