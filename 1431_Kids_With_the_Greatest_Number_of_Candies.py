# First find the largest Candy and then compare it with each candy + extraCandy ,
# if it is greater than or Equal then append true otherwise False . and return the result.

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxCandies = max(candies)
        result = []

        for candy in candies:
            if candy + extraCandies >= maxCandies :
                result.append(True)
            else : 
                result.append(False)

        return result
