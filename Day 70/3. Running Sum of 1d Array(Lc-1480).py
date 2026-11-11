#code

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        n=len(nums)
        ans=[0]*n
        ans[0]=nums[0]
        for i in range(1,n):
            ans[i]=nums[i]+ans[i-1]
        return ans

"""https://leetcode.com/problems/running-sum-of-1d-array/"""
        




#Intuition




I will use an auxiliary array to store the running sum.

First, I calculate the length of the input array and initialize another array of the same size with zeros.

Since the running sum of the first element is the element itself, I assign nums[0] to ans[0].

Then, I iterate through the input array starting from index 1.

At each index, I add the current element of the input array to the previous running sum stored in the answer array.

In other words, ans[i] = nums[i] + ans[i-1].

Finally, I return the answer array containing the running sums.
