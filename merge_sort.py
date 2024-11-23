def merge(a, start, mid, end):
    comparisons_count = initializations_count = i = j = 0
    l = a[start: mid + 1]
    r = a[mid + 1:end + 1]
    k = start

    while i < len(l) and j < len(r):
        comparisons_count += 1
        if l[i] < r[j]:
            a[k] = l[i]
            i += 1
        else:
            a[k] = r[j]
            j += 1
        k += 1
        initializations_count += 1

    while i < len(l):
        a[k] = l[i]
        initializations_count += 1
        i += 1
        k += 1

    return comparisons_count, initializations_count


def merge_sort_func(a, start, end):
    comparisons_count = initializations_count = 0
    if start < end:
        mid = (start + end) // 2
        c_l, i_l = merge_sort_func(a, start, mid)
        c_r, i_r = merge_sort_func(a, mid + 1, end)
        c_m, i_m = merge(a, start, mid, end)
        comparisons_count += c_l + c_r + c_m
        initializations_count += i_r + i_l + i_m
    return comparisons_count, initializations_count


def merge_sort(arr):
    return merge_sort_func(arr, 0, len(arr))


