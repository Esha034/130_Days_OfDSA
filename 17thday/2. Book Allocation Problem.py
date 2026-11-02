#optimal solution

class Solution:
    def isPossible(self, arr, n, m, maxpages):
        pages = 0
        students = 1

        for i in range(n):
            if pages + arr[i] <= maxpages:
                pages += arr[i]
            else:
                students += 1
                pages = arr[i]
                if students > m:
                    return False
        return True

    def findpages(self, arr, n, m):
       
        if m > n:
            return -1

        low = max(arr)
        high = sum(arr)
        res = -1

        while low <= high:
            mid = low + (high - low) // 2
            if self.isPossible(arr, n, m, mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res


# # Driver code
# if __name__ == "__main__":
#     arr = [25, 46, 28, 49, 24]
#     n = len(arr)
#     m = 4  # number of students

#     obj = Solution()
#     result = obj.findpages(arr, n, m)
#     print("Minimum number of pages =", result)

            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#bruteforce
        # def countStudents(arr, pages):
        #     n = len(arr)  # size of array
        #     students = 1
        #     pagesStudent = 0
        #     for i in range(n):
        #         if pagesStudent + arr[i] <= pages:
        #             pagesStudent += arr[i]
        #         else:
        #             students += 1
        #             pagesStudent = arr[i]
        # return students

        # def findPages(arr, n, m):
        #     if m > n:
        #         return -1

        #     low = max(arr)
        #     high = sum(arr)

        #     for pages in range(low, high + 1):
        #         if countStudents(arr, pages) == m:
        #             return pages
        #     return low
    
