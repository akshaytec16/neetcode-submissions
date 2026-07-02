class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        r= [0]*n
        p= [0]*n
        s= [0]*n
        p[0]=s[n-1]=1
        for i in range(1,n):
            p[i]= nums[i-1] * p[i-1]
        for i in range(n-2,-1,-1):
            s[i]= nums[i+1] * s[i+1]
        for i in range(n):
            r[i]= s[i] * p[i]
        return r








