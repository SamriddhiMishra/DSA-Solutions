# Binary Search

def bin_search(arr, l, r, k):
    if l>r:
        return False
    mid = (l+r)//2
    if arr[mid] == k:
        return True
    elif k < arr[mid]:
        return bin_search(arr, l, mid-1, k)
    elif k > arr[mid]:
        return bin_search(arr, mid+1, r, k)
    
arr = [1,2,3]
print(bin_search(arr, 0, len(arr)-1, 6))