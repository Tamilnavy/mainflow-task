def fibonaccisequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fibsequence = [0, 1]
    for i in range(2, n):
        fibsequence.append(fibsequence[-1] + fibsequence[-2])
    
    return fibsequence
n = int(input("Enter the number of Fibonacci numbers to generate: "))
print(fibonaccisequence(n))
