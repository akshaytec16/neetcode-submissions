class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res=0
        l=0
        r=len(heights)-1
        while l<r:
            w= r-l
            h= min(heights[l],heights[r])
            a=w*h
            res=max(res,a)
            if heights[l] < heights[r]:
                l +=1
            else:
                r -=1
        return res