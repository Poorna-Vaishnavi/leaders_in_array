def find_leaders(A):
    leaders = []
    max_right = float('-inf')
    n = len(A)
    
    for i in range(n-1, -1, -1):
        if A[i] > max_right:
            leaders.append(A[i])
            max_right = A[i]
    
    leaders.reverse()
    return leaders

# Get input from the user
A = list(map(int, input("Enter the elements of array A : ").split()))

output = find_leaders(A)
print("Leaders in array A:", output)