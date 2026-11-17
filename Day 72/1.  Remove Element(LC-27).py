#slow pointer approcah

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


#Intuition:

Here:
- i (fast pointer) explores every element.
- k (slow pointer) tracks where the next valid element should be placed.
- Whenever nums[i] != val, we copy it to nums[k] and increment k.
-Finally we return K, which contains number 












#two pointer approcah

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        n=len(nums)
        l,r=0,n-1

        while l<=r:
            if nums[l]==val and nums[r]!=val:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
            elif nums[l]==val and nums[r]==val:
                r-=1
            else:
                l+=1
        return l



#complexity :

Let n be the length of the input array.

Time:	O(n)	Each pointer moves only in one direction, at most n iterations in total.
Auxiliary space:	(O(1))	We modify the input array directly without creating another array.





#Intuition

I am using the two-pointer approach with one pointer starting from the beginning and another from the end of the array.

My objective is to move all occurrences of the given value towards the right side while keeping all the elements that are not equal to the target value in the first part of the array.

I compare the elements at both pointers.

If the left element equals the target and the right element does not, I swap them and move both pointers inward.

If both elements equal the target, I move only the right pointer backward.

If the left element is not equal to the target, it is already in the correct position, so I move the left pointer forward.

I continue this process until the two pointers cross each other.

Finally, I return the left pointer, which represents the number of valid elements

