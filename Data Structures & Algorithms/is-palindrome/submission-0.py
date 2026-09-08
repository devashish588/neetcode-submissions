class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newStr = ""

        # Step 1: Clean up the string
        for c in s:
            if c.isalnum():
                newStr += c.lower()
                
        # Step 2: FIXED - Added 'return' to send the result back
        return newStr == newStr[::-1]
