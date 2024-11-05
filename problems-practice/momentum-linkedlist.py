"""Problem Statement -:  
        Ratul made a linked list, a list made of n nodes, where every node has two variables, the velocity and the mass of a particle.

        Since all the particles have the velocity in the same direction, find the total momentum of the entity made by the particles from the linked list.

        list of n nodes with 2 values velocity and mass

        
        
        Constraints :

        1<=n<=10000
        1<=m,v<=100
        

        Input format:

        First line containing n, number of nodes
        Then n lines containing the mass and the velocity space separated.
        

        Output Format:

        Single integer denoting the momentum
        

        Sample Input:

        4

        1 3

        2 4

        2 3

        4 5

        Sample Output:

        37
    """
    
node=int(input())
momentum=0

for node in range(node):
    mass,vel=map(int,input().split())
    momentum+=(mass*vel)
print(momentum)
    