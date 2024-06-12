import random
import math

#program to generate a random list
rand_list=[]
n=10
for i in range(n):
	rand_list.append(random.randint(0,99))
print(rand_list)

count= sum(rand_list)
average= count/len(rand_list)

print("Sum=", count)
print("Average=", average)