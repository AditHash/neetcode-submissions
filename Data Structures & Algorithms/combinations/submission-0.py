class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        temp = []

        def helper(start):
            # Base case
            if len(temp) == k:
                ans.append(temp.copy())
                return

            for i in range(start, n + 1):
                # Choose
                temp.append(i)

                # Explore
                helper(i + 1)

                # Backtrack
                temp.pop()

        helper(1)

        return ans