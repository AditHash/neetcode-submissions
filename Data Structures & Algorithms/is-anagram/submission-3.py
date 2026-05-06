class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = {}
        seen_t = {}
        for c in s:
            if c in seen_s:
                seen_s[c] += 1
            else:
                seen_s[c] = 1
        
        for d in t:
            if d in seen_t:
                seen_t[d] += 1
            else:
                seen_t[d] = 1
            
        if seen_s == seen_t:
            return True
        else:
            return False