#print all prime numbers between 2 and N

N=int(input("What is the value of N?: "))

for num in range(2,N+1):
    prime=True
    for i in range(2,num):
        if num % 2 == 0:
            prime=False
            break
    if prime:
        print(num)