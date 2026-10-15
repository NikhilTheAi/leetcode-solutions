class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        rev = 0

        if num < 0 : 
            return False;

        while num > 0 : 
            ld = num % 10
            rev = rev * 10 + ld 
            num = num // 10
        
        return x == rev
