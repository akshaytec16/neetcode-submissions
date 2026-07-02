class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        n=len(nums)
        r= [1] * n
        for i in range(1,n):
            r[i] = nums[i-1] * r[i-1]
        c=1
        for i in range(n-1,-1,-1):
            r[i] *=c
            c *= nums[i]
        return r








