#Optimal approach: Three Pointers (From the End)

We will use three pointers:
- i = m - 1: Points to the last valid element of nums1.
- j = n - 1: Points to the last element of nums2.
- k = m + n - 1: Points to the last available position in nums1.


Why start from the end?

Because nums1 already has extra empty positions at the end. 
We can fill those positions with the largest elements first, without overwriting the original elements that we still need to compare.




#code


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i=m-1
        j=n-1
        k=m+n-1
        while j>=0:
            if i>=0 and nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1










#Intuition

I will use a three-pointer approach to merge the two sorted arrays in-place.

Since nums1 has extra space at the end, I will start merging from the end to avoid overwriting the existing elements.

I initialize three pointers:
- i points to the last valid element of nums1.
- j points to the last element of nums2.
- k points to the last available position in nums1.
I compare the elements at i and j.

If nums1[i] is greater, I place it at nums1[k] and decrement i.

Otherwise, I place nums2[j] at nums1[k] and decrement j.

After every placement, I decrement k to move to the previous available position.

I continue until all elements of nums2 are placed.

Finally, nums1 contains the merged sorted array









#Complexity analysis:

Let m and n represent the lengths of the valid portions of the two arrays.

Complexity	Value	      Explanation
Time	      (O(m+n))      Each pointer moves only from right to left.
space	       (O(1))	       We modify nums1 directly without creating another array.
