def quicksort(arr: list,left: int,right: int):
    
    if left < right:
        print(arr[left:right+1])
        pi = partition(arr, left, right)
        quicksort(arr,left,pi-1)
        quicksort(arr,pi+1, right)
                
def partition(arr: list,left: int,right: int):
    pivot = arr[right]
    
    i = left - 1
    
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i+1

arr = [7,1,5,2,4,8,9,0,3,6]

print(f"\nOriginal: {arr}\n")

quicksort(arr, 0, len(arr) - 1)

print(f"\nQuickSort: {arr}")