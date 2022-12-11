# Divide and Conquer algorithm
# o(n)
# Split array in half
# Call Merge Sort on each half to sort them recursively
# Merge both sorted halves into one sorted array


def merge_sort(arr):
    if len(arr) > 1:
        # From the beginning of the array to the middle.
        left_arr = arr[:len(arr)//2]
        # From the middle of the array to the end.
        right_arr = arr[len(arr)//2:]
        # Recursion
        merge_sort(left_arr)
        merge_sort(right_arr)
        # Merge step
        # left_arr index
        i = 0
        # right_arr index
        j = 0
        # new_merged_arr index
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
        else:
            return arr


if __name__ == "__main__":
    arr = [30, 33, 36, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    print("Array after sorting", merge_sort(arr))
