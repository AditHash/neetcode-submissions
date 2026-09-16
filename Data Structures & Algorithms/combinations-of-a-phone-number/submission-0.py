class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        ans = []
        temp = ""

        mapping = [
            "",
            ".",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
        ]

        def helper(digits: str, ans: List[str], temp: str, start: int) -> None:

            # Base case
            if start == len(digits):
                ans.append(temp)
                return

            letters = mapping[int(digits[start])]

            for i in range(len(letters)):

                # Choose
                temp += letters[i]

                # Explore
                helper(digits, ans, temp, start + 1)

                # Backtrack
                temp = temp[:-1]

        if digits == "":
            return []

        helper(digits, ans, temp, 0)

        return ans