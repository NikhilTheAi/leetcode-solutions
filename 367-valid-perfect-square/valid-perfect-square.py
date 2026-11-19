class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        beg = 1
        end = num

        while beg <= end:
            mid = (beg + end) // 2

            if mid * mid == num:
                return True
            elif mid * mid > num:
                end = mid - 1
            else:
                beg = mid + 1

        return False