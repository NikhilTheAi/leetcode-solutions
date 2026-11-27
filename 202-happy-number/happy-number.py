class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while True:
            total = 0

            while n != 0:
                ld = n % 10
                total += ld ** 2
                n //= 10

            if total == 1:
                return True

            n = total

            if n in seen:
                return False

            seen.add(n)