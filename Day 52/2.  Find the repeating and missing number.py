#optimal

class Solution:
    def findMissingRepeatingNumbers(self, nums):
        n = len(nums)

        S = n*(n+1)//2
        S2 = n*(n+1)*(2*n+1)//6

        actual_S = sum(nums)
        actual_S2 = sum(x*x for x in nums)

        val1 = actual_S - S        # A - B
        val2 = actual_S2 - S2      # A² - B²

        val2 = val2 // val1        # A + B

        A = (val1 + val2) // 2     # repeating
        B = A - val1               # missing

        return [A, B]




#better

class Solution:
    def findMissingRepeatingNumbers(self, nums):

        res=[]
        n=len(nums)
        expected_sum=n*(n+1)//2
        actual_sum=0
        mp={}

        # find repeating
        for num in nums:
            actual_sum+=num
            if num not in mp:
                mp[num]=1
            else:
                mp[num]+=1

        for key in mp:
            if mp[key]==2:
                repeating=key
                res.append(repeating)

        missing=expected_sum-(actual_sum-repeating)
        res.append(missing)
        return res
