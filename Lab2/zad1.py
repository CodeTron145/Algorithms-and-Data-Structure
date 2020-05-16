# coding=utf-8
import random
import timeit
import sys
from pip._vendor.distlib.compat import raw_input

def insertion_sort(arr):
    global comp_counter, shift_counter, length
    for i in range(1, length):
        key = arr[i]
        j = i - 1
        print("Wykonujemy porównanie sąsiednich elementów...")
        comp_counter += 1
        while j >= 0 and arr[j] > key:
            print("Przestawiamy większy element o 1 w prawo...")
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
        print("Wykonujemy porównanie sąsiednich elementów...")
        comp_counter += 1
        while j >= 0 and arr[j] < key:
            print("Przestawiamy większy element o 1 w lewo...")
            shift_counter += 1
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    global comp_counter, shift_counter
    print("Wykonujemy porównanie...")
    comp_counter += 1
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        print("Wykonujemy porównanie...")
        comp_counter += 1
        while i < len(L) and j < len(R):
            print("Wykonujemy porównanie...")
            comp_counter += 1
            if L[i] < R[j]:
                print("Przestawiamy większy element o 1 w prawo...")
                shift_counter += 1
                arr[k] = L[i]
                i += 1
            else:
                print("Przestawiamy większy element o 1 w prawo...")
                shift_counter += 1
                arr[k] = R[j]
                j += 1
            k += 1

        print("Wykonujemy porównanie...")
        comp_counter += 1
        while i < len(L):
            print("Przestawiamy większy element o 1 w prawo...")
            shift_counter += 1
            arr[k] = L[i]
            i += 1
            k += 1

        print("Wykonujemy porównanie...")
        comp_counter += 1
        while j < len(R):
            print("Przestawiamy większy element o 1 w prawo...")
            shift_counter += 1
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


def merge_sort_reverse(arr):
    global comp_counter, shift_counter
    print("Wykonujemy porównanie...")
    comp_counter += 1
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort_reverse(L)
        merge_sort_reverse(R)

        i = j = k = 0
        print("Wykonujemy porównanie...")
        comp_counter += 1
        while i < len(L) and j < len(R):
            print("Wykonujemy porównanie...")
            comp_counter += 1
            if L[i] < R[j]:
                print("Przestawiamy większy element o 1 w lewo...")
                shift_counter += 1
                arr[k] = R[j]
                j += 1
            else:
                print("Przestawiamy większy element o 1 w lewo...")
                shift_counter += 1
                arr[k] = L[i]
                i += 1
            k += 1

        print("Wykonujemy porównanie...")
        comp_counter += 1
        while i < len(L):
            print("Przestawiamy większy element o 1 w lewo...")
            shift_counter += 1
            arr[k] = L[i]
            i += 1
            k += 1

        print("Wykonujemy porównanie...")
        comp_counter += 1
        while j < len(R):
            print("Przestawiamy większy element o 1 w lewo...")
            shift_counter += 1
            arr[k] = R[j]
            j += 1
            k += 1


def quick_sort(arr):
    quick_sort_act(arr, 0, len(arr)-1)


def quick_sort_reverse(arr):
    quick_sort_act_reverse(arr, 0, len(arr)-1)


def get_pivot(arr, low, high):
    global comp_counter
    mid = (high + low) // 2
    pivot = high
    print("Wykonujemy porównanie...")
    comp_counter += 1
    if arr[low] < arr[mid]:
        print("Wykonujemy porównanie...")
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
    print("Przestawiamy element...")
    shift_counter += 1
    arr[pivot_index], arr[low] = arr[low], arr[pivot_index]
    border = low

    for i in range(low, high+1):
        print("Wykonujemy porównanie...")
        comp_counter += 1
        if arr[i] < pivot_value:
            border += 1
            print("Przestawiamy element...")
            shift_counter += 1
            arr[i], arr[border] = arr[border], arr[i]
    print("Przestawiamy element...")
    shift_counter += 1
    arr[low], arr[border] = arr[border], arr[low]

    return border


def partition_reverse(arr, low, high):
    global shift_counter, comp_counter
    pivot_index = get_pivot(arr, low, high)
    pivot_value = arr[pivot_index]
    print("Przestawiamy element...")
    shift_counter += 1
    arr[pivot_index], arr[low] = arr[low], arr[pivot_index]
    border = low

    for i in range(low, high+1):
        print("Wykonujemy porównanie...")
        comp_counter += 1
        if arr[i] > pivot_value:
            border += 1
            print("Przestawiamy element...")
            shift_counter += 1
            arr[i], arr[border] = arr[border], arr[i]
    print("Przestawiamy element...")
    shift_counter += 1
    arr[low], arr[border] = arr[border], arr[low]

    return border


def quick_sort_act_reverse(arr, low, high):
    global comp_counter
    print("Wykonujemy porównanie...")
    comp_counter += 1
    if low < high:
        p = partition_reverse(arr, low, high)
        quick_sort_act_reverse(arr, low, p-1)
        quick_sort_act_reverse(arr, p + 1, high)


def quick_sort_act(arr, low, high):
    global comp_counter
    print("Wykonujemy porównanie...")
    comp_counter += 1
    if low < high:
        p = partition(arr, low, high)
        quick_sort_act(arr, low, p-1)
        quick_sort_act(arr, p + 1, high)

def dual_pivot_quick_sort(arr):
    dual_pivot_quick_sort_act(arr, 0, len(arr) - 1)


def dual_pivot_quick_sort_act(arr, low, high):
    global comp_counter, shift_counter
    print("Wykonujemy porówanie...")
    comp_counter += 1
    if high <= low:
        return
    p = low
    q = high
    k = p + 1
    h = k
    l = q - 1
    if arr[p] > arr[q]:
        print("Przestawiamy element...")
        shift_counter += 1
        arr[p], arr[q] = arr[q], arr[p]
    while k <= l:
        print("Wykonujemy porówanie...")
        comp_counter += 1
        if arr[k] < arr[p]:
            print("Przestawiamy element...")
            shift_counter += 1
            arr[h], arr[k] = arr[k], arr[h]
            h += 1
            k += 1
        elif arr[k] > arr[q]:
            print("Przestawiamy element...")
            shift_counter += 1
            arr[k], arr[l] = arr[l], arr[k]
            l -= 1
        else:
            k += 1
    h -= 1
    l += 1
    print("Przestawiamy element...")
    shift_counter += 1
    arr[p], arr[h] = arr[h], arr[p]
    print("Przestawiamy element...")
    shift_counter += 1
    arr[q], arr[l] = arr[l], arr[q]
    dual_pivot_quick_sort_act(arr, low, h - 1)
    dual_pivot_quick_sort_act(arr, h + 1, l - 1)
    dual_pivot_quick_sort_act(arr, l + 1, high)

def dual_pivot_quick_sort_reverse(arr):
    dual_pivot_quick_sort_act_reverse(arr, 0, len(arr) - 1)


def dual_pivot_quick_sort_act_reverse(arr, low, high):
    global comp_counter, shift_counter
    print("Wykonujemy porówanie...")
    comp_counter += 1
    if high <= low:
        return
    p = low
    q = high
    k = p + 1
    h = k
    l = q - 1
    if arr[p] < arr[q]:
        print("Przestawiamy element...")
        shift_counter += 1
        arr[p], arr[q] = arr[q], arr[p]
    while k <= l:
        print("Wykonujemy porówanie...")
        comp_counter += 1
        if arr[k] > arr[p]:
            print("Przestawiamy element...")
            shift_counter += 1
            arr[h], arr[k] = arr[k], arr[h]
            h += 1
            k += 1
        elif arr[k] < arr[q]:
            print("Przestawiamy element...")
            shift_counter += 1
            arr[k], arr[l] = arr[l], arr[k]
            l -= 1
        else:
            k += 1
    h -= 1
    l += 1
    print("Przestawiamy element...")
    shift_counter += 1
    arr[p], arr[h] = arr[h], arr[p]
    print("Przestawiamy element...")
    shift_counter += 1
    arr[q], arr[l] = arr[l], arr[q]
    dual_pivot_quick_sort_act_reverse(arr, low, h - 1)
    dual_pivot_quick_sort_act_reverse(arr, h + 1, l - 1)
    dual_pivot_quick_sort_act_reverse(arr, l + 1, high)


def hybrid_quick_sort(arr):
    hybrid_quick_sort_act(arr, 0, len(arr) - 1)


def hybrid_quick_sort_act(arr, low, high):
    global comp_counter
    print("Wykonujemy porówanie...")
    comp_counter += 1
    while low < high:
        print("Wykonujemy porówanie...")
        comp_counter += 1
        if high - low < 10:
            insertion_sort(arr)
            break
        else:
            p = partition(arr, low, high)
            print("Wykonujemy porówanie...")
            comp_counter += 1
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
    print("Wykonujemy porówanie...")
    comp_counter += 1
    while low < high:
        print("Wykonujemy porówanie...")
        comp_counter += 1
        if high - low < 10:
            insertion_sort_reverse(arr)
            break
        else:
            p = partition_reverse(arr, low, high)
            print("Wykonujemy porówanie...")
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


array_length = int(raw_input())
nums = list(map(int, raw_input().split(" ")))
while len(nums) != array_length:
    print("Nieprawidłowa liczba elementów w ciągu! Sprobuj ponownie!")
    nums = list(map(int, raw_input().split(" ")))
length = len(nums)
comp_counter = 0
shift_counter = 0
timer = 0
is_sorted = False


if sys.argv[2] == "insert" and sys.argv[4] == "<=":
    timer = timeit.Timer(lambda: insertion_sort(nums)).timeit(number=1)
    is_sorted = if_sorted(nums)
elif sys.argv[2] == "insert" and sys.argv[4] == ">=":
    timer = timeit.Timer(lambda: insertion_sort_reverse(nums)).timeit(number=1)
    is_sorted = if_sorted_reverse(nums)
elif sys.argv[2] == "merge" and sys.argv[4] == "<=":
    timer = timeit.Timer(lambda: merge_sort(nums)).timeit(number=1)
    is_sorted = if_sorted(nums)
elif sys.argv[2] == "merge" and sys.argv[4] == ">=":
    timer = timeit.Timer(lambda: merge_sort_reverse(nums)).timeit(number=1)
    is_sorted = if_sorted_reverse(nums)
elif sys.argv[2] == "quick" and sys.argv[4] == "<=":
    timer = timeit.Timer(lambda: quick_sort(nums)).timeit(number=1)
    is_sorted = if_sorted(nums)
elif sys.argv[2] == "quick" and sys.argv[4] == ">=":
    timer = timeit.Timer(lambda: quick_sort_reverse(nums)).timeit(number=1)
    is_sorted = if_sorted_reverse(nums)
elif sys.argv[2] == "dual_pivot" and sys.argv[4] == "<=":
    timer = timeit.Timer(lambda: dual_pivot_quick_sort(nums)).timeit(number=1)
    is_sorted = if_sorted(nums)
elif sys.argv[2] == "dual_pivot" and sys.argv[4] == ">=":
    timer = timeit.Timer(lambda: dual_pivot_quick_sort_reverse(nums)).timeit(number=1)
    is_sorted = if_sorted_reverse(nums)
elif sys.argv[2] == "hybrid" and sys.argv[4] == "<=":
    timer = timeit.Timer(lambda: hybrid_quick_sort(nums)).timeit(number=1)
    is_sorted = if_sorted(nums)
elif sys.argv[2] == "hybrid" and sys.argv[4] == ">=":
    timer = timeit.Timer(lambda: hybrid_quick_sort_reverse(nums)).timeit(number=1)
    is_sorted = if_sorted_reverse(nums)

print("\nDługość listy: " + str(length))
print("Ilość przestawień: " + str(shift_counter))
print("Ilość porównań: " + str(comp_counter))
print("Czas działania algorytmu: " + str(timer) + " sekund")
print("Czy jest posortowany: " + str(is_sorted))
print("Posortowany ciąg: " + str(nums))
