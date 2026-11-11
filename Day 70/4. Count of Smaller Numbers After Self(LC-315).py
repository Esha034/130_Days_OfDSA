# bruteforce approach


class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        n=len(nums)
        counts=[0]*n
        for i in range(n):
            for j in range(i+1,n):
                if nums[j]<nums[i]:
                    counts[i]+=1
        return counts  



# Complexity:

Time Complexity: (O(n^2)) — The nested loops can compare every element with all elements to its right.

Space Complexity: (O(n)) — The counts array stores n results.
