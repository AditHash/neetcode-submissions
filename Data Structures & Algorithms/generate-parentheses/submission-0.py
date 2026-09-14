class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def helper(res: List[str], n: int, bopen: int, bclose: int, s: str):
            
            # Base case
            if (bopen == n) and (bclose == n):
                res.append(s)
                return
            # add a (
            if (bopen < n):
                helper(res, n, bopen + 1, bclose, s + "(")
            # or add )
            if(bopen > bclose):
                helper(res, n, bopen, bclose + 1, s + ")")

        helper(res, n, 0, 0, "")

        return res

