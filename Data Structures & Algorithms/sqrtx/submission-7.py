class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            # Avoid calculating mid * mid
            if mid <= x // mid:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans