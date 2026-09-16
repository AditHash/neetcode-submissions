class Solution:
    def partition(self, s: str) -> List[List[str]]:

        ans = []
        temp = []

        def isPalindrome(s: str, l: int, h: int) -> bool:
            # Palindrome Function 
            while l < h:
                if s[l] != s[h]:
                    return False

                l = l + 1
                h = h - 1

            return True

        n = len(s)

        def helper(s: str, res: List[List[str]], temp: List[str], start: int) -> None:

            # Base case
            if start == n:
                res.append(temp.copy())
                return

            for i in range(start, n):

                if isPalindrome(s, start, i):

                    # Choose
                    temp.append(s[start:i + 1])

                    # Explore
                    helper(s, res, temp, i + 1)

                    # Backtrack
                    temp.pop()

        helper(s, ans, temp, 0)

        return ans