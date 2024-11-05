"""
    Question 6: Help of Prepsters
    Problem Statement-: Arnab has given me a challenge. 
    I have to calculate the number of numbers which are less than a certain value n, and have exactly k set bits in its binary form. 
    As you are a Prepster like me, help me write a code that will take input for n and k and give the expected output.

    

    Constraints :

    1<=n<=10000
    1<=k<=10
    Input Format :

    First line containing n and k space separated
    Output Format :

    Number of numbers present in a single line
    

    Sample Input:

    7 2

    Sample Output:

    3

    Explanation:

    011,110,101 -> These three numbers.
    
    """
    
    
result=0
n,k=map(int,input().split())
l=len(bin(n)[2:])
def challenge(i,s,L):
    global l 
    global result
    if(L>l):
        return
    if i==0 :
        result+=1 
    if s!="":
        if n<int(s,2):
            return
    challenge(i-1,s+"1",L+1)
    challenge(i,s+"0",L+1)
    


challenge(k-1,"1",1)
print(result)
