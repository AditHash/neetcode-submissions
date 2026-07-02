class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}

        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        
        max_odd = 0
        min_even = None

        for count in freq.values():
            if count % 2 == 1:
                if count > max_odd:
                    max_odd = count
            else:
                if min_even is None or count < min_even:
                    min_even = count
        return max_odd - min_even


