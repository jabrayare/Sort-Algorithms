from typing import List
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
