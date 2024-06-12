#Python program to generate a list of random numbers

import random

rand_list=[]
n=10
for i in range(n):
    rand_list.append(random.randint(0,9))
print("The random list is:")
print(rand_list)


#Python program to merge-sort two arrays from a single random list
def mergeSort(rand_list):
    if len(rand_list) > 1:

        # Create sub_array1 and sub_array2 
        mid = len(rand_list)//2
        sub_array1 = rand_list[:mid]
        sub_array2 = rand_list[mid:]

        # Sort the two halves
        mergeSort(sub_array1)
        mergeSort(sub_array2)
       
        # Initial values for pointers that we use to keep track of where we are in each array
        i = j = k = 0

        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i] < sub_array2[j]:
                rand_list[k] = sub_array1[i]
                i += 1
            else:
                rand_list[k] = sub_array2[j]
                j += 1
            k += 1

        while i < len(sub_array1):
            rand_list[k] = sub_array1[i]
            i += 1
            k += 1

        while j < len(sub_array2):
            rand_list[k] = sub_array2[j]
            j += 1
            k += 1

mergeSort(rand_list)
print("The sorted array is:")
print(rand_list)


#credit for code framework: https://www.scaler.com/topics/merge-sort-in-python/
