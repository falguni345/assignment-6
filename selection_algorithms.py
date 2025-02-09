import random

# Selection Algorithms
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def randomized_partition(arr, low, high):
    rand_index = random.randint(low, high)
    arr[high], arr[rand_index] = arr[rand_index], arr[high]
    return partition(arr, low, high)

def randomized_select(arr, low, high, k):
    if low == high:
        return arr[low]
    pivot_index = randomized_partition(arr, low, high)
    rank = pivot_index - low + 1
    if k == rank:
        return arr[pivot_index]
    elif k < rank:
        return randomized_select(arr, low, pivot_index - 1, k)
    else:
        return randomized_select(arr, pivot_index + 1, high, k - rank)

def median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k-1]
    sublists = [arr[i:i+5] for i in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]
    median_of_median = median_of_medians(medians, len(medians)//2 + 1)
    pivot = partition(arr, 0, len(arr) - 1)
    rank = pivot + 1
    if k == rank:
        return arr[pivot]
    elif k < rank:
        return median_of_medians(arr[:pivot], k)
    else:
        return median_of_medians(arr[pivot+1:], k - rank)
