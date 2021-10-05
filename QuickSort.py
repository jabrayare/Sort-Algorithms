from typing import List
"""
Sort array A[i..j] of size n = j − i + 1 by partitioning the array about an arbitrary value and sorting both parts of the partition.
"""
def quick_sort(nums: List[int], n):
  pass

arr = [4,9,1,3,0]
# print(arr)
n = len(arr)
quick_sort(arr, n-1)
print(arr)

"""
Best Case: O(nlog(n))
Expected Case: O(nlog(n))
Worst Case: O(n^2)
"""