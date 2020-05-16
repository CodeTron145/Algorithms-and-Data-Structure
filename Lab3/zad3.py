# coding=utf-8
import random
import timeit
from pip._vendor.distlib.compat import raw_input

comp_counter = 0


def binary_search(arr, left, right, v):
    global comp_counter

    comp_counter += 1
    if right >= left:

        mid = left + (right - left) // 2

        if arr[mid] == v:
            print("Element has been found!")
            return 1
        elif arr[mid] > v:
            return binary_search(arr, left, mid - 1, v)
        else:
            return binary_search(arr, mid + 1, right, v)
    else:
        print("Element hasn't been founded!")
        return 0

print("Wprowadz rozmiar ciagu:", end=" ")
n = int(raw_input())
print("Wprowadz liczbę, ktora chcesz znalezc:", end=" ")
v = int(raw_input())

arr = sorted([random.randint(0, n) for i in range(n)])
arr1 = arr[:n//2]
print(arr, arr1)
timer1 = timeit.Timer(lambda: binary_search(arr, 0, len(arr) - 1, v)).timeit(number=1)
comp_counter1 = comp_counter
comp_counter = 0
timer2 = timeit.Timer(lambda: binary_search(arr1, 0, len(arr1) - 1, v)).timeit(number=1)
factor_comp = comp_counter1 - comp_counter
factor_time = timer1 - timer2
print("Czynnik O(1) dla n = " + str(n) + "(ilosc powtorzen)" + " wynosi " + str(factor_comp))
print("Czynnik O(1) dla n = " + str(n) + "(czas)" + " wynosi " + str(factor_time))