# Simple Extract the last digit and add them in total and mul in mul and return mul - total .

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        total = 0
        mul = 1
        copy = n
        while copy > 0 :
            ld = copy % 10
            total += ld
            mul *= ld
            copy = copy // 10
        return mul - total
    
        
