#Python program to generate a list of random numbers

import random

rand_list=[]
n=8
for i in range(n):
    rand_list.append(random.randint(0,100))
print("The random list is:")
print(rand_list)


#Python program to sort using the insertion-sort algorithm
def InsertionSort(rand_list):
  
    # traversing the array from 1 to length of the array(rand_list)
    for i in range(1, len(rand_list)):
  
        temp = rand_list[i]
  
        # Shift elements of array[0 to i-1], that are
        # greater than temp, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and temp < rand_list[j] :
                rand_list[j+1] = rand_list[j]
                j -= 1
        rand_list[j+1] = temp

InsertionSort(rand_list)
print("Array after sorting:")
print(rand_list)

#credit for code framework:https://www.scaler.com/topics/insertion-sort-in-python/