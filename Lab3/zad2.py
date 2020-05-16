# coding=utf-8

import random
import sys
import numpy as np
import logging
import math
from pip._vendor.distlib.compat import raw_input

length = 0
shift_counter = 0
comp_counter = 0
pivots = []


def select_sort(arr):
    global shift_counter, comp_counter
    for i in range(0, len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            logging.info("Wykonujemy porównanie...")
            comp_counter += 1
            if arr[j] < arr[min_index]:
                min_index = j
        logging.info("Wykonujemy porównanie...")
        comp_counter += 1
        if min_index != i:
            logging.info("Przestawiamy element...")
            shift_counter += 1
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def partition(arr, left, right):
    global shift_counter, comp_counter
    x = arr[right]
    i = left
    for j in range(left, right):
        logging.info("Wykonujemy porównanie...")
        comp_counter += 1
        if arr[j] <= x:
            logging.info("Przestawiamy element...")
            shift_counter += 1
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    logging.info("Przestawiamy element...")
    shift_counter += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


def randomized_select_sort(arr, k):
    return randomized_select_sort_act(arr, 0, len(arr) - 1, k)


def randomized_select_sort_act(arr, left, right, k):
    global comp_counter

    logging.info("Wykonujemy porównanie...")
    comp_counter += 1
    if 0 < k <= right - left + 1:

        pivot = partition(arr, left, right)
        logging.info("Adding new pivot to array")
        pivots.append(pivot)

        logging.info("Wykonujemy porównanie...")
        comp_counter += 1
        if pivot - left == k - 1:
            return arr[pivot]

        logging.info("Wykonujemy porównanie...")
        comp_counter += 1
        if pivot - left > k - 1:
            return randomized_select_sort_act(arr, left, pivot - 1, k)

        return randomized_select_sort_act(arr, pivot + 1, right, k - pivot + left - 1)


logging.basicConfig(level=logging.INFO)
n = int(raw_input())
k = int(raw_input())
arr1 = []
arr2 = []

if sys.argv[1] == '-r':
    arr1 = random.sample(range(100), n)
    arr2 = arr1.copy()

if sys.argv[1] == '-p':
    arr1 = np.random.permutation(n)
    arr2 = arr1.copy()


select_sort(arr1)
print('\n')
logging.info("Długość listy: " + str(n))
logging.info("Ilość przestawień: " + str(shift_counter))
logging.info("Ilość porównań: " + str(comp_counter))
logging.info("Posortowany ciąg: " + str(arr1) + '\n')

shift_counter = 0
comp_counter = 0

arr_previous = arr2.copy()

result = randomized_select_sort(arr2, k)
print('\n')
logging.info("Długość listy: " + str(n))
logging.info("Ilość przestawień: " + str(shift_counter))
logging.info("Ilość porównań: " + str(comp_counter))
logging.info("Kolejne pivoty: " + str(pivots) + '\n')

for i in range(len(arr_previous)):
    if arr_previous[i] == result:
        print("["+str(result)+"]", end=" ")
    elif arr_previous[i] != result:
        print(arr_previous[i], end=" ")
print("\n")

