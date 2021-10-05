from typing import List
"""
Sort array A[i..j] of size n = j − i + 1 by splitting the array, recursively sorting, and then merging the two parts.
"""
def merge_sort(arr: List[int], i: int, j:int):
  if i < j:
    midp = (i+j)//2
    merge_sort(arr, i, midp)
    merge_sort(arr, midp+1, j)
    merge(arr, i, midp, j)

def copy(arr:List[int], i:int, j:int, B:List[int]):
  p = 1
  for k in range(i, j):
    B[p] = arr[k]
    p += 1
  B[p] = float('inf')

def merge(arr:List[int], first:int, midp:int, last:int):
  l = [] * len(arr)
  r = [] * len(arr)
  copy(arr, first, midp,l)  
  copy(arr, midp+1, last,r) 
  i = 0
  j = 0
  for k in range(first, last):
    if l[i] < r[j]:
      arr[k] = l[i]
      i += 1
    else:
      arr[k] = r[i]
      j += 1
arr = [4,9,1,3,0]
# print(arr)
n = len(arr)
merge_sort(arr, 0, n-1)
print(arr)

"""
Best Case: O(nlog(n))
Expected Case: O(nlog(n))
Worst Case: O(nlog(n))

"""