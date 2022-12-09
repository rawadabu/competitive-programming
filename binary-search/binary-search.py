def binary_search(arr, x):
    # My code here
    s = 0
    e = len(arr) - 1

    while s <= e:
        mid = (s + e)//2
        if arr[mid] < x :
            s = mid + 1
        elif arr[mid] > x:
            e = mid - 1
        else:
            return mid
    return -1


if __name__ == "__main__":
    arr = [ 2, 3, 4, 10, 40 ]
    x = 11

    my_index = binary_search(arr,x)
    if my_index == -1:
        print("Element is not existed")
    else:
        print("Element at index", str(my_index))