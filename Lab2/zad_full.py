#!/usr/bin/env python
# coding=utf-8

import random
import timeit
import sys
# import matplotlib.pyplot as plot
import pandas as pd
import xlwt
import xlrd
import os

nums = random.sample(range(20), 10)
length = 0
comp_counter = 0
shift_counter = 0
timer = 0
is_sorted = False
time_ex = []
shifts = []
compares = []
size_array = []


def insertion_sort(arr):
    global comp_counter, shift_counter, length
    for i in range(1, length):
        key = arr[i]
        j = i - 1
        comp_counter += 1
        while j >= 0 and arr[j] > key:
            shift_counter += 1
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr


def insertion_sort_reverse(arr):
    global length, comp_counter, shift_counter
    for i in range(1, length):
        key = arr[i]
        j = i - 1
        comp_counter += 1
        while j >= 0 and arr[j] < key:
            shift_counter += 1
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    global comp_counter, shift_counter
    comp_counter += 1
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        comp_counter += 1
        while i < len(L) and j < len(R):
            comp_counter += 1
            if L[i] < R[j]:
                shift_counter += 1
                arr[k] = L[i]
                i += 1
            else:
                shift_counter += 1
                arr[k] = R[j]
                j += 1
            k += 1

        comp_counter += 1
        while i < len(L):
            shift_counter += 1
            arr[k] = L[i]
            i += 1
            k += 1

        comp_counter += 1
        while j < len(R):
            shift_counter += 1
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


def merge_sort_reverse(arr):
    global comp_counter, shift_counter
    comp_counter += 1
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort_reverse(L)
        merge_sort_reverse(R)

        i = j = k = 0
        comp_counter += 1
        while i < len(L) and j < len(R):
            comp_counter += 1
            if L[i] < R[j]:
                shift_counter += 1
                arr[k] = R[j]
                j += 1
            else:
                shift_counter += 1
                arr[k] = L[i]
                i += 1
            k += 1

        comp_counter += 1
        while i < len(L):
            shift_counter += 1
            arr[k] = L[i]
            i += 1
            k += 1

        comp_counter += 1
        while j < len(R):
            shift_counter += 1
            arr[k] = R[j]
            j += 1
            k += 1


def quick_sort(arr):
    quick_sort_act(arr, 0, len(arr) - 1)


def quick_sort_reverse(arr):
    quick_sort_act_reverse(arr, 0, len(arr) - 1)


def get_pivot(arr, low, high):
    global comp_counter
    mid = (high + low) // 2
    pivot = high
    comp_counter += 1
    if arr[low] < arr[mid]:
        comp_counter += 1
        if arr[mid] < arr[high]:
            pivot = mid
    elif arr[low] < arr[high]:
        pivot = low
    return pivot


def partition(arr, low, high):
    global comp_counter, shift_counter
    pivot_index = get_pivot(arr, low, high)
    pivot_value = arr[pivot_index]
    shift_counter += 1
    arr[pivot_index], arr[low] = arr[low], arr[pivot_index]
    border = low

    for i in range(low, high + 1):
        comp_counter += 1
        if arr[i] < pivot_value:
            border += 1
            shift_counter += 1
            arr[i], arr[border] = arr[border], arr[i]
    shift_counter += 1
    arr[low], arr[border] = arr[border], arr[low]

    return border


def partition_reverse(arr, low, high):
    global shift_counter, comp_counter
    pivot_index = get_pivot(arr, low, high)
    pivot_value = arr[pivot_index]
    shift_counter += 1
    arr[pivot_index], arr[low] = arr[low], arr[pivot_index]
    border = low

    for i in range(low, high + 1):
        comp_counter += 1
        if arr[i] > pivot_value:
            border += 1
            shift_counter += 1
            arr[i], arr[border] = arr[border], arr[i]
    shift_counter += 1
    arr[low], arr[border] = arr[border], arr[low]

    return border


def quick_sort_act_reverse(arr, low, high):
    global comp_counter
    comp_counter += 1
    if low < high:
        p = partition_reverse(arr, low, high)
        quick_sort_act_reverse(arr, low, p - 1)
        quick_sort_act_reverse(arr, p + 1, high)


def quick_sort_act(arr, low, high):
    global comp_counter
    comp_counter += 1
    if low < high:
        p = partition(arr, low, high)
        quick_sort_act(arr, low, p - 1)
        quick_sort_act(arr, p + 1, high)


def dual_pivot_quick_sort(arr):
    dual_pivot_quick_sort_act(arr, 0, len(arr) - 1)


def dual_pivot_quick_sort_act(arr, low, high):
    global comp_counter, shift_counter
    comp_counter += 1
    if high <= low:
        return
    p = low
    q = high
    k = p + 1
    h = k
    l = q - 1
    if arr[p] > arr[q]:
        shift_counter += 1
        arr[p], arr[q] = arr[q], arr[p]
    while k <= l:
        comp_counter += 1
        if arr[k] < arr[p]:
            shift_counter += 1
            arr[h], arr[k] = arr[k], arr[h]
            h += 1
            k += 1
        elif arr[k] > arr[q]:
            shift_counter += 1
            arr[k], arr[l] = arr[l], arr[k]
            l -= 1
        else:
            k += 1
    h -= 1
    l += 1
    shift_counter += 1
    arr[p], arr[h] = arr[h], arr[p]
    shift_counter += 1
    arr[q], arr[l] = arr[l], arr[q]
    dual_pivot_quick_sort_act(arr, low, h - 1)
    dual_pivot_quick_sort_act(arr, h + 1, l - 1)
    dual_pivot_quick_sort_act(arr, l + 1, high)


def dual_pivot_quick_sort_reverse(arr):
    dual_pivot_quick_sort_act_reverse(arr, 0, len(arr) - 1)


def dual_pivot_quick_sort_act_reverse(arr, low, high):
    global comp_counter, shift_counter
    comp_counter += 1
    if high <= low:
        return
    p = low
    q = high
    k = p + 1
    h = k
    l = q - 1
    if arr[p] < arr[q]:
        shift_counter += 1
        arr[p], arr[q] = arr[q], arr[p]
    while k <= l:
        comp_counter += 1
        if arr[k] > arr[p]:
            shift_counter += 1
            arr[h], arr[k] = arr[k], arr[h]
            h += 1
            k += 1
        elif arr[k] < arr[q]:
            shift_counter += 1
            arr[k], arr[l] = arr[l], arr[k]
            l -= 1
        else:
            k += 1
    h -= 1
    l += 1
    shift_counter += 1
    arr[p], arr[h] = arr[h], arr[p]
    shift_counter += 1
    arr[q], arr[l] = arr[l], arr[q]
    dual_pivot_quick_sort_act_reverse(arr, low, h - 1)
    dual_pivot_quick_sort_act_reverse(arr, h + 1, l - 1)
    dual_pivot_quick_sort_act_reverse(arr, l + 1, high)


def hybrid_quick_sort(arr):
    hybrid_quick_sort_act(arr, 0, len(arr) - 1)


def hybrid_quick_sort_act(arr, low, high):
    while low < high:
        if high - low < 10:
            insertion_sort(arr)
            break
        else:
            p = partition(arr, low, high)

            if p - low < high - p:
                hybrid_quick_sort_act(arr, low, p - 1)
                low = p + 1
            else:
                hybrid_quick_sort_act(arr, p + 1, high)
                high = p - 1


def hybrid_quick_sort_reverse(arr):
    hybrid_quick_sort_act_reverse(arr, 0, len(arr) - 1)


def hybrid_quick_sort_act_reverse(arr, low, high):
    global comp_counter
    comp_counter += 1
    while low < high:
        comp_counter += 1
        if high - low < 10:
            insertion_sort_reverse(arr)
            break
        else:
            p = partition_reverse(arr, low, high)
            comp_counter += 1
            if p - low < high - p:
                hybrid_quick_sort_act_reverse(arr, low, p - 1)
                low = p + 1
            else:
                hybrid_quick_sort_act_reverse(arr, p + 1, high)
                high = p - 1


def if_sorted_reverse(a):
    return a == sorted(a, reverse=True)


def if_sorted(a):
    return a == sorted(a)


# Zapisanie info do pliku
def excel_data():
    sys.setrecursionlimit(10100)
    algorithm_name = ''
    wb = xlwt.Workbook()
    ws = wb.add_sheet("Algorithms")
    heading_xf = xlwt.easyxf('font: bold on; align: wrap on, vert centre, horiz center')
    headings = ['Nazwa', 'Dlugosc', 'Czas', 'L_Porownan', 'L_Przestawien']
    global timer, comp_counter, shift_counter, length, time_ex, shifts, compares, size_array
    for i in range(100, 10100, 100):
        nums = random.sample(range(i), i)
        length = len(nums)
        if sys.argv[2] == "insert" and sys.argv[4] == "<=":
            for j in range(int(sys.argv[7])):
                timer = timeit.Timer(lambda: insertion_sort(nums)).timeit(number=1)
                time_ex.append(timer)
                shifts.append(shift_counter)
                compares.append(comp_counter)
                size_array.append(length)
            algorithm_name = "Insertion sort"
        elif sys.argv[2] == "insert" and sys.argv[4] == ">=":
            for j in range(int(sys.argv[7])):
                timer = timeit.Timer(lambda: insertion_sort_reverse(nums)).timeit(number=1)
                time_ex.append(timer)
                shifts.append(shift_counter)
                compares.append(comp_counter)
                size_array.append(length)
            algorithm_name = "Insertion sort"
        elif sys.argv[2] == "merge" and sys.argv[4] == "<=":
            for j in range(int(sys.argv[7])):
                timer = timeit.Timer(lambda: merge_sort(nums)).timeit(number=1)
                time_ex.append(timer)
                shifts.append(shift_counter)
                compares.append(comp_counter)
                size_array.append(length)
            algorithm_name = "Merge sort"
        elif sys.argv[2] == "merge" and sys.argv[4] == ">=":
            for j in range(int(sys.argv[7])):
                timer = timeit.Timer(lambda: merge_sort_reverse(nums)).timeit(number=1)
                time_ex.append(timer)
                shifts.append(shift_counter)
                compares.append(comp_counter)
                size_array.append(length)
            algorithm_name = "Merge sort"
        elif sys.argv[2] == "quick" and sys.argv[4] == "<=":
            for j in range(int(sys.argv[7])):
                timer = timeit.Timer(lambda: quick_sort(nums)).timeit(number=1)
                time_ex.append(timer)
                shifts.append(shift_counter)
                compares.append(comp_counter)
                size_array.append(length)
            algorithm_name = "Quick sort"
        elif sys.argv[2] == "quick" and sys.argv[4] == ">=":
            for j in range(int(sys.argv[7])):
                timer = timeit.Timer(lambda: quick_sort_reverse(nums)).timeit(number=1)
                time_ex.append(timer)
                shifts.append(shift_counter)
                compares.append(comp_counter)
                size_array.append(length)
            algorithm_name = "Quick sort"
        elif sys.argv[2] == "dual_pivot" and sys.argv[4] == "<=":
            for j in range(int(sys.argv[7])):
                timer = timeit.Timer(lambda: dual_pivot_quick_sort(nums)).timeit(number=1)
                time_ex.append(timer)
                shifts.append(shift_counter)
                compares.append(comp_counter)
                size_array.append(length)
            algorithm_name = 'Dual pivot...'
        elif sys.argv[2] == "dual_pivot" and sys.argv[4] == ">=":
            for j in range(int(sys.argv[7])):
                timer = timeit.Timer(lambda: dual_pivot_quick_sort_reverse(nums)).timeit(number=1)
                time_ex.append(timer)
                shifts.append(shift_counter)
                compares.append(comp_counter)
                size_array.append(length)
            algorithm_name = 'Dual pivot...'
        elif sys.argv[2] == "hybrid" and sys.argv[4] == "<=":
            for j in range(int(sys.argv[7])):
                timer = timeit.Timer(lambda: hybrid_quick_sort(nums)).timeit(number=1)
                time_ex.append(timer)
                shifts.append(shift_counter)
                compares.append(comp_counter)
                size_array.append(length)
            algorithm_name = 'Hybrid'
        elif sys.argv[2] == "hybrid" and sys.argv[4] == ">=":
            for j in range(int(sys.argv[7])):
                timer = timeit.Timer(lambda: hybrid_quick_sort_reverse(nums)).timeit(number=1)
                time_ex.append(timer)
                shifts.append(shift_counter)
                compares.append(comp_counter)
                size_array.append(length)
            algorithm_name = 'Hybrid'

    for cols, value in enumerate(headings):
        ws.write(0, cols, value, heading_xf)

    rows = 1
    cols = 0

    for i in range(0, len(size_array)):
        ws.write(rows, cols, algorithm_name)
        rows += 1

    rows = 1
    cols += 1
    for items in size_array:
        ws.write(rows, cols, items)
        rows += 1

    rows = 1
    cols += 1
    for items in time_ex:
        ws.write(rows, cols, items)
        rows += 1

    rows = 1
    cols += 1
    for items in compares:
        ws.write(rows, cols, items)
        rows += 1

    rows = 1
    cols += 1
    for items in shifts:
        ws.write(rows, cols, items)
        rows += 1

    file_name = sys.argv[6]
    print(file_name)
    wb.save(file_name)


# Zależność liczby porównań od długości n
def comp_n():
    global path
    table = 0
    if sys.argv[2] == "insert":
        table = pd.read_excel(path + "insertSort.xls")
    elif sys.argv[2] == "merge":
        table = pd.read_excel(path + "mergeSort.xls")
    elif sys.argv[2] == "quick":
        table = pd.read_excel(path + "quickSort.xls")
    elif sys.argv[2] == "dual_pivot":
        table = pd.read_excel(path + "dual_pivotSort.xls")
    elif sys.argv[2] == "hybrid":
        table = pd.read_excel(path + "hybrid.xls")

    table_new = table[['Dlugosc', 'L_Porownan']]
    table_new.plot(x='Dlugosc', y='L_Porownan')
    plot.show()


# Zależność liczby przestawień od długości n
def shift_n():
    table = 0
    if sys.argv[2] == "insert":
        table = pd.read_excel(path + "insertSort.xls")
    elif sys.argv[2] == "merge":
        table = pd.read_excel(path + "mergeSort.xls")
    elif sys.argv[2] == "quick":
        table = pd.read_excel(path + "quickSort.xls")
    elif sys.argv[2] == "dual_pivot":
        table = pd.read_excel(path + "dual_pivotSort.xls")
    elif sys.argv[2] == "hybrid":
        table = pd.read_excel(path + "hybrid.xls")

    table_new = table[['Dlugosc', 'L_Przestawien']]
    table_new.plot(x='Dlugosc', y='L_Przestawien')
    plot.show()


# Zależność czasu od długości n
def time_n():
    table = 0
    if sys.argv[2] == "insert":
        table = pd.read_excel(path + "insertSort.xls")
    elif sys.argv[2] == "merge":
        table = pd.read_excel(path + "mergeSort.xls")
    elif sys.argv[2] == "quick":
        table = pd.read_excel(path + "quickSort.xls")
    elif sys.argv[2] == "dual_pivot":
        table = pd.read_excel(path + "dual_pivotSort.xls")
    elif sys.argv[2] == "hybrid":
        table = pd.read_excel(path + "hybrid.xls")

    table_new = table[['Czas', 'Dlugosc']]
    table_new.plot(x='Dlugosc', y='Czas')
    plot.show()


# Zależność liczby porównań/n od długości n
def d_comp_n():
    table = 0
    if sys.argv[2] == "insert":
        table = pd.read_excel(path + "insertSort.xls")
    elif sys.argv[2] == "merge":
        table = pd.read_excel(path + "mergeSort.xls")
    elif sys.argv[2] == "quick":
        table = pd.read_excel(path + "quickSort.xls")
    elif sys.argv[2] == "dual_pivot":
        table = pd.read_excel(path + "dual_pivotSort.xls")
    elif sys.argv[2] == "hybrid":
        table = pd.read_excel(path + "hybrid.xls")

    table_new = table[['L_Porownan', 'Dlugosc']]
    table_new['L_Porownan'] = table['L_Porownan'].div(table['Dlugosc'])

    table_new.plot(x='Dlugosc', y='L_Porownan')
    plot.show()


# Zależność liczby przestawień/n od długości n
def d_shift_n():
    table = 0
    if sys.argv[2] == "insert":
        table = pd.read_excel(path + "insertSort.xls")
    elif sys.argv[2] == "merge":
        table = pd.read_excel(path + "mergeSort.xls")
    elif sys.argv[2] == "quick":
        table = pd.read_excel(path + "quickSort.xls")
    elif sys.argv[2] == "dual_pivot":
        table = pd.read_excel(path + "dual_pivotSort.xls")
    elif sys.argv[2] == "hybrid":
        table = pd.read_excel(path + "hybrid.xls")

    table_new = table[['L_Porownan', 'Dlugosc']]
    table_new['L_Przestawien'] = table['L_Przestawien'].div(table['Dlugosc'])

    table_new.plot(x='Dlugosc', y='L_Przestawien')
    plot.show()


excel_data()

# Dla rysowania wykresów Pan powinny wpisać ścieżkę gdzie znajduje plik.xls
path = "/home/s246389/Lab2/"

# Zależność liczby porównań od długości n
# comp_n()

# Zależność liczby przestawień od długości n
# shift_n()

# Zależność czasu od długości n
# time_n()

# Zależność liczby porównań/n od długości n
# d_comp_n()

# Zależność liczby przestawień/n od długości n
# d_shift_n()
