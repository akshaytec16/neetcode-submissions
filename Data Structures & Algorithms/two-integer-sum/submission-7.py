class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s={}
        for i,n in enumerate(nums):
            d = target - n
            if d in s:
                return [s[d],i]
            s[n]=i
        return []