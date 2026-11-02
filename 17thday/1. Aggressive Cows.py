class Solution:
    def aggressiveCows(self, nums, k):

        # Step 1: Sort manually
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]


        n = len(nums)
        # Step 2: to check if min distance possible
        def possiblemin(mindis):
            cow = 1  
            laststallpos = nums[0]

            for i in range(1, n):  
                if nums[i] - laststallpos >= mindis:
                    cow += 1
                    laststallpos = nums[i]
                if cow == k:
                    return True
            return False

        # Step 3: Binary search on answer
        low = 1
        high = nums[-1] - nums[0]
        res = 0

        while low <= high:
            mid = low + (high - low) // 2

            if possiblemin(mid):  
                res = mid          # store answer and try for larger distance
                low = mid + 1
            else:
                high = mid - 1     # reduce distance if not possible

        return res
