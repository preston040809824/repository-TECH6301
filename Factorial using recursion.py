def recur_fact(n):
    if n==1:
        return n
    else:
        return n*recur_fact(n-1)

base=7

print("The factorial of", base, "is", recur_fact(base))