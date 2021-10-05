from typing import List
"""
Sort array A[1..n] of size n by splitting array into sorted
and unsorted portions. Iteratively insert elements from the
unsorted portion into the sorted portion
"""
def Insertion_sort(nums: List[int], n):
  for i in range(1, n):
    key = nums[i]
    
    j = i - 1
    while j >= 0 and key < nums[j]:
      nums[j+1] = nums[j]
      j -= 1
    
    nums[j+1] = key
    print(nums)
arr = [4,9,1,3,0]
# print(arr)
n = len(arr)
Insertion_sort(arr, n)
print(arr)

"""
Best Case: O(n)
Expected Case: O(n^2)
Worst Case: O(n^2)

"""