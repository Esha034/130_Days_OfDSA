#code

class Solution:
    def countOccurrences(self, nums, target):
        def find_first(nums, target):
            low, high = 0, len(nums)-1
            first = -1
            while low <= high:
                mid = low + (high-low)//2
                if nums[mid] == target:
                    first = mid
                    high = mid - 1  # search left
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return first

        def find_last(nums, target):
            low, high = 0, len(nums)-1
            last = -1
            while low <= high:
                mid = low + (high-low)//2
                if nums[mid] == target:
                    last = mid
                    low = mid + 1  # search right
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return last


        first = find_first(nums, target)
        last = find_last(nums, target)
        if first == -1:
            return 0
        return (last - first) + 1
 


