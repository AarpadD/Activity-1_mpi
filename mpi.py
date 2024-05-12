import timeit
import random
import heapq


def generate_random_list(size, lower_limit, upper_limit):
    return [random.randint(lower_limit, upper_limit) for _ in range(size)]

def generate_nearly_sorted_list(size, lower_limit, upper_limit, swap_percent=0.05):
    sorted_list = list(range(lower_limit, lower_limit + size))
    swap_count = int(size * swap_percent)
    for _ in range(swap_count):
        i, j = random.sample(range(size), 2)
        sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]
    return sorted_list


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        equal_to_pivot = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + equal_to_pivot + quick_sort(right)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def heap_sort(arr):
    h = []
    for value in arr:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for _ in range(len(h))]


def radix_sort(arr):
    RADIX = 10
    placement = 1
    max_digit = max(arr)

    while placement < max_digit:
        buckets = [list() for _ in range(RADIX)]
        for i in arr:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                arr[a] = i
                a += 1
        placement *= RADIX
    return arr


def count_sort(arr):
    max_val = max(arr)
    m = max_val + 1
    count = [0] * m
    for a in arr:
        count[a] += 1
    i = 0
    for a in range(m):
        for _ in range(count[a]):
            arr[i] = a
            i += 1
    return arr



sizes = [100, 500, 1000, 5000]
lower_limit = 0
upper_limit = 1000

for size in sizes:
    random_list = generate_random_list(size=size, lower_limit=lower_limit, upper_limit=upper_limit)
    nearly_sorted_list = generate_nearly_sorted_list(size=size, lower_limit=lower_limit, upper_limit=upper_limit)

    for list_name, current_list in [('random_list', random_list), ('nearly_sorted_list', nearly_sorted_list)]:
        execution_time_bubble_sort = timeit.timeit(lambda: bubble_sort(current_list.copy()), number=100)
        print(f"For size {size} with {list_name}, Execution time of bubbleSort: {execution_time_bubble_sort} seconds.")

        execution_time_merge_sort = timeit.timeit(lambda: merge_sort(current_list.copy()), number=100)
        print(f"For size {size} with {list_name}, Execution time of mergeSort: {execution_time_merge_sort} seconds.")

        execution_time_quick_sort = timeit.timeit(lambda: quick_sort(current_list.copy()), number=100)
        print(f"For size {size} with {list_name}, Execution time of quickSort: {execution_time_quick_sort} seconds.")

        execution_time_insertion_sort = timeit.timeit(lambda: insertion_sort(current_list.copy()), number=100)
        print(f"For size {size} with {list_name}, Execution time of insertionSort: {execution_time_insertion_sort} seconds.")

        execution_time_selection_sort = timeit.timeit(lambda: selection_sort(current_list.copy()), number=100)
        print(f"For size {size} with {list_name}, Execution time of selectionSort: {execution_time_selection_sort} seconds.")

        execution_time_heap_sort = timeit.timeit(lambda: heap_sort(current_list.copy()), number=100)
        print(f"For size {size} with {list_name}, Execution time of heapSort: {execution_time_heap_sort} seconds.")

        execution_time_radix_sort = timeit.timeit(lambda: radix_sort(current_list.copy()), number=100)
        print(f"For size {size} with {list_name}, Execution time of radixSort: {execution_time_radix_sort} seconds.")

        execution_time_count_sort = timeit.timeit(lambda: count_sort(current_list.copy()), number=100)
        print(f"For size {size} with {list_name}, Execution time of countingSort: {execution_time_count_sort} seconds.")