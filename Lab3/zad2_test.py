# coding=utf-8
import random
import sys
import numpy as np
import math
from pip._vendor.distlib.compat import raw_input

comp_counter = 0


def select_sort(arr):
    global comp_counter
    for i in range(0, len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            comp_counter += 1
            if arr[j] < arr[min_index]:
                min_index = j
        comp_counter += 1
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def partition(arr, left, right):
    global comp_counter
    x = arr[right]
    i = left
    for j in range(left, right):
        comp_counter += 1
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[right] = arr[right], arr[i]
    return i


def randomized_select_sort(arr, k):
    return randomized_select_sort_act(arr, 0, len(arr) - 1, k)


def randomized_select_sort_act(arr, left, right, k):
    global comp_counter

    comp_counter += 1
    if 0 < k <= right - left + 1:

        pivot = partition(arr, left, right)

        comp_counter += 1
        if pivot - left == k - 1:
            return arr[pivot]

        comp_counter += 1
        if pivot - left > k - 1:
            return randomized_select_sort_act(arr, left, pivot - 1, k)

        return randomized_select_sort_act(arr, pivot + 1, right, k - pivot + left - 1)


n = int(raw_input())
k = int(raw_input())
arr1 = []
arr2 = []
select_comp = []
r_select_comp = []

repeats = 1000
sys.setrecursionlimit(1100)
for i in range(repeats):
    if sys.argv[1] == '-r':
        arr1 = random.sample(range(100), n)
        arr2 = arr1.copy()

    if sys.argv[1] == '-p':
        arr1 = np.random.permutation(n)
        arr2 = arr1.copy()

    select_sort(arr1)
    select_comp.append(comp_counter)
    comp_counter = 0

    randomized_select_sort(arr2, k)
    r_select_comp.append(comp_counter)
    comp_counter = 0

min_comp = min(select_comp)
max_comp = max(select_comp)
print("SELECT: Minimalna liczba porównań dla " + str(n) + " elementów: " + str(min_comp))
print("SELECT: Maksymalna liczba porównań dla " + str(n) + " elementów: " + str(max_comp) + "\n")

min_comp = min(r_select_comp)
max_comp = max(r_select_comp)
print("RANDOMIZED SELECT: Minimalna liczba porównań dla " + str(n) + " elementów: " + str(min_comp))
print("RANDOMIZED SELECT: Maksymalna liczba porównań dla " + str(n) + " elementów: " + str(max_comp) + "\n")

average1 = sum(select_comp) // repeats
average2 = sum(r_select_comp) // repeats
standard_deviation1 = 0
standard_deviation2 = 0
for i in range(repeats):
    standard_deviation1 += (select_comp[i] - average1) ** 2
    standard_deviation2 += (r_select_comp[i] - average2) ** 2
standard_deviation1 = math.sqrt(standard_deviation1 // repeats)
standard_deviation2 = math.sqrt(standard_deviation2 // repeats)

print("SELECT: Średnia liczba porównań dla " + str(n) + " elementów wynosi " + str(average1))
print("SELECT: Standardowe odchylenie dla " + str(n) + " elementów wynosi " + str(standard_deviation1) + "\n")

print("RANDOMIZED SELECT: Średnia liczba porównań dla " + str(n) + " elementów wynosi " + str(average2))
print("RANDOMIZED SELECT: Standardowe odchylenie dla " + str(n) + " elementów wynosi " + str(standard_deviation2) + "\n")


