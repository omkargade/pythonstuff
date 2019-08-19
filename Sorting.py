# visualizing sorting of a list of random values from 1 to 100 via different algorithms
#sorting algorithms taken from internet

import matplotlib.pyplot as plt
import random

def plot(res):
    plt.plot(res,'ro')
    plt.plot(res)
    plt.pause(0.000000001)
    plt.clf()
plt.show()

def Rand(num):
    res = list(range(1,num))
    random.shuffle(res)
    return res,res.copy(),res.copy(),res.copy()

def bubblesort(list):
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp
                plot(list)


def insertion_sort(InputList):
    for i in range(1, len(InputList)):
        j = i - 1
        nxt_element = InputList[i]
        # Compare the current element with next one

        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j + 1] = InputList[j]
            j = j - 1
        InputList[j + 1] = nxt_element
        plot(InputList)


def shellSort(input_list):
    gap = len(input_list) // 2
    while gap > 0:

        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i
            # Sort the sub list for this gap

            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]
                j = j - gap
            input_list[j] = temp
            plot(input_list)

        # Reduce the gap for the next element

        gap = gap // 2

def selection_sort(input_list):

    for idx in range(len(input_list)):

        min_idx = idx
        for j in range( idx +1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j
        plot(input_list)
        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]


def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
# Find the middle point and devide it
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))

# Merge the sorted halves

def merge(left_half,right_half):

    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])

    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res;

l,l1,l2,l3,l4 = Rand(100)
bubblesort(l)
insertion_sort(l1)
shellSort(l2)
selection_sort(l3)
merge_sort(l4)
plt.close()