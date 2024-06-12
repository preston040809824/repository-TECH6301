def recur_fib(n):
    if n <= 1:
        return n
    else:
        return (recur_fib(n-1)+recur_fib(n-2))
    
nterms = 10

if nterms <= 0:
    print("Enter a positive integer")
else:
    print("Fibonacci series: ")
    for i in range(nterms):
        print(recur_fib(i))