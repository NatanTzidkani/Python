def max_heapify(a, i, heap_size):
    comparisons_count = initializations_count = 0
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i
    comparisons_count += 1
    if l < heap_size and a[l] > a[largest]:
        largest = l

    comparisons_count += 1
    if r < heap_size and a[r] > a[largest]:
        largest = r

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        initializations_count += 2
        c, i = max_heapify(a, largest, heap_size)
        comparisons_count += c
        initializations_count += i

    return comparisons_count, initializations_count


def build_max_heap(a):
    comparisons_count = initializations_count = 0

    for i in range(len(a) // 2 - 1, -1, -1):
        c, i_count = max_heapify(a, i, len(a))
        comparisons_count += c
        initializations_count += i_count

    return comparisons_count, initializations_count


def heap_sort(arr):
    comparisons_count = initializations_count = 0

    c_build, i_build = build_max_heap(arr)
    comparisons_count += c_build
    initializations_count += i_build

    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        initializations_count += 2
        c_heapify, i_heapify = max_heapify(arr, 0, i)
        comparisons_count += c_heapify
        initializations_count += i_heapify

    return comparisons_count, initializations_count

