# Bubble sort algorithm
# Iterations and comparison between two variables till the array is sorted


def bubble_sort(arr):
    indexing_length = len(arr) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if arr[i] > arr[i+1]:
                sorted = False
                # Swap
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


if __name__ == "__main__":
    arr = [30, 33, 36, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    print("Array after sorting", bubble_sort(arr))
