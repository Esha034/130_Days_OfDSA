class Solution:
    def maxLen(self, arr):
        n=len(arr)
        max_len=0
        mp={}
        pre_sum=0
        for i in range(n):
            pre_sum+=arr[i]

            if pre_sum==0:
                max_len=i+1

            if pre_sum-0 in mp:
                length=i-mp[pre_sum-0]
                max_len=max(length,max_len)

            if pre_sum not in mp:
                mp[pre_sum]=i
                
        return max_len
       
