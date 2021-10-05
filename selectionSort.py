from typing import List
"""
Sort array A[1..n] of size n by recursively selecting
the maximum element and placing it at the end of the array
"""
def selectionSort(arr: List[int], n: int):
  if n < 1:
    return 
  for i in range(0, n):
    if arr[i] > arr[n]:
      arr[i], arr[n] = arr[n], arr[i]
  selectionSort(arr, n-1)

arr = [4,9,1,3,0]
# print(arr)
n = len(arr)
selectionSort(arr, n-1)
print(arr)

"""
Best Case: O(n^2)
Expected Case: O(n^2)
Worst Case: O(n^2)

"""