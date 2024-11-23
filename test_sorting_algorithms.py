import random
import matplotlib.pyplot as plt
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from heap_sort import heap_sort


def test_sort_algorithms(algorithms, array_sizes):
    results = {alg_name: {"comparisons": [], "initializations": []} for alg_name in algorithms.keys()}

    for size in array_sizes:
        arr = [random.randint(1, 1000) for _ in range(size)]
        for alg_name, alg_func in algorithms.items():
            arr_copy = arr.copy()

            if alg_name == "Merge Sort":
                comp_count, init_count = alg_func(arr_copy)
            elif alg_name == "Quick Sort":
                comp_count, init_count = alg_func(arr_copy)
            elif alg_name == "Heap Sort":
                comp_count, init_count = alg_func(arr_copy)
            else:

                comp_count, init_count = alg_func(arr_copy)

            results[alg_name]["comparisons"].append(comp_count)
            results[alg_name]["initializations"].append(init_count)
    return results


algorithms = {
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Heap Sort": heap_sort
}

array_sizes = [10, 50, 100, 200, 500]
results = test_sort_algorithms(algorithms, array_sizes)

def plot_results(results, array_sizes):
    for metric in ["comparisons", "initializations"]:
        plt.figure(figsize=(10, 6))
        for alg_name, metrics in results.items():
            plt.plot(array_sizes, metrics[metric], marker='o', label=alg_name)

        plt.title(f"{metric.capitalize()} vs Array Size")
        plt.xlabel("Array Size")
        plt.ylabel(metric.capitalize())
        plt.legend()
        plt.grid(True)
        plt.show()

plot_results(results, array_sizes)
