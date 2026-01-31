from collections import Counter
from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = sorted(Counter(nums).items(), key=lambda x: (x[1], -x[0]))
        ans = []

        for tup in count:
            for i in range(tup[1]):
                ans.append(tup[0])
        return ans
