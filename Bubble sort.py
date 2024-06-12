#Python program to generate a list of random numbers

import random

rand_list=[]
n=10
for i in range(n):
    rand_list.append(random.randint(0,9))
print("The random list is:")
print(rand_list)


# Python program for implementation of Bubble Sort


def bubbleSort(rand_list):

      for i in range(n-1): 
        swapped = False
        for j in range(0, n-i-1):

             if rand_list[j] > rand_list[j + 1]:
                swapped = True
                rand_list[j], rand_list[j + 1] = rand_list[j + 1], rand_list[j]

        if not swapped:
             return


bubbleSort(rand_list)

print("The sorted array is:")
for i in range(len(rand_list)):
    print("% d" % rand_list[i], end=" ")