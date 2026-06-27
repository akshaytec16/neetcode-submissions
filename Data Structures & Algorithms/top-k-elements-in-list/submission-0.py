class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = Counter(nums)
        c= s.most_common(k)
        return [num for num, freq in c]