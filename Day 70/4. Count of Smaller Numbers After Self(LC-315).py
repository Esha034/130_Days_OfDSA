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




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
3. Optimized approach: Fenwick Tree (Binary Indexed Tree)
Recommended: O(n log n)
The key observation is:

We need to count how many elements smaller than the current element have already appeared on its right.

Instead of checking every element individually, we can maintain a data structure that efficiently counts previously processed elements.

We use a Fenwick Tree (Binary Indexed Tree) to achieve this.
How does it work?
We process the array from right to left.
1. Coordinate-compress the values so that each distinct number gets a rank.
2. Create a Fenwick Tree to maintain the frequency of processed elements.
3. For each element, query how many previously processed elements have a smaller rank.
4. Store that result in counts[i].
5. Update the Fenwick Tree with the current element's rank.

#code


class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        n = len(nums)
        counts = [0] * n

        # Coordinate compression
        sorted_nums = sorted(set(nums))
        rank = {num: i + 1 for i, num in enumerate(sorted_nums)}

        # Fenwick Tree
        m = len(sorted_nums)
        bit = [0] * (m + 1)

        def update(i):
            while i <= m:
                bit[i] += 1
                i += i & -i

        def query(i):
            total = 0
            while i > 0:
                total += bit[i]
                i -= i & -i
            return total

        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            r = rank[nums[i]]

            counts[i] = query(r - 1)
            update(r)

        return counts


4. Dry run of optimized approach
Input:
nums = [5, 2, 6, 1]



Step 1: Coordinate compression

Sort the unique elements:
sorted_nums = [1, 2, 5, 6]



Assign ranks:
Number	Rank
1	1
2	2
5	3
6	4

Initially:
bit = [0, 0, 0, 0, 0]counts = [0, 0, 0, 0]



Step 2: Traverse from right to left

We process 1 → 6 → 2 → 5.
Current element	Rank	Query	Smaller elements on right	Count
