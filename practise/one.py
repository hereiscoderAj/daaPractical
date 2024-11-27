def binarySearch(arr, left, right, key):
    while left <= right:
        mid = left + (right - left)//2

        if arr[mid] == key:
            return arr[mid]
        
        if arr[mid] < key:
            left = mid + 1

        if arr[mid] > key:
            right = mid - 1

    return -1

def main():
    size = int(input("Enter the size of the array: "))


    if size <= 0 :
        print(f"Enter the valid size for the array")
        return
    
    for i in size:
        arr =int(input("Enter {i} integer: "))

    arr.sort()
    print ("Sorted array:", arr)

    key = int(input("Enter the key element: "))
    result = binarySearch(arr, 0, arr(len)-1, key)

    if __name__ == "__main__" :
        main()

        