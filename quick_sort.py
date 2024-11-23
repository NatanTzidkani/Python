import random


def partition(a, p, r):
    comparisons_count = initializations_count = 0
    x = a[r]
    i = p - 1
    for j in range(p, r):
        comparisons_count += 1
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
            initializations_count += 2
    a[i + 1], a[r] = a[r], a[i + 1]
    initializations_count += 2
    return i + 1, comparisons_count, initializations_count


def randomized_partition(a, p, r):
    comparisons_count = initializations_count = 0
    i = random.randint(p, r)
    a[i], a[r] = a[r], a[i]
    comparisons_count += 2

    q, c_part, i_part = partition(a, p, r)
    comparisons_count += c_part
    initializations_count += i_part

    return q, comparisons_count, initializations_count


def randomized_quicksort(a, p, r):
    comparisons_count = initializations_count = 0
    if p < r:
        q, c_rand_part, i_rand_part = randomized_partition(a, p, r)
        comparisons_count += c_rand_part
        initializations_count += i_rand_part
        c_left, i_left = randomized_quicksort(a, p, q - 1)
        c_right, i_right = randomized_quicksort(a, q + 1, r)
        comparisons_count += c_left + c_right
        initializations_count += i_left + i_right

    return comparisons_count, initializations_count


def quick_sort(arr):
    return randomized_quicksort(arr, 0, len(arr) - 1)


