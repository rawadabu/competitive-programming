# A function that returns how many k the array is shifted

def shifted_array(arr, s, e):
    if s == e:
        return arr[s]
    mid = (s+e)//2
    if arr[mid] > arr[mid+1]:
        return arr[mid]
    else:
        if arr[mid] < arr[s]:
            return shifted_array(arr, s, mid-1)
        else:
            return shifted_array(arr, mid+1, e)


if __name__ == "__main__":
    arr = [30, 33, 36, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    s = 0
    e = len(arr) - 1
    print("The maximum number is", shifted_array(arr, s, e))
    print("The array is shifted by", arr.index(shifted_array(arr, s, e))+1, "shifts.")
