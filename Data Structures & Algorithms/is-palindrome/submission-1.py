class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Put your left pointer at the start, right pointer at the end
        left = 0
        right = len(s) - 1

        # Step 2: Keep moving until the pointers meet in the middle
        while left < right:
            
            # If the left character is not a letter or number, skip it
            while left < right and not s[left].isalnum():
                left += 1
                
            # If the right character is not a letter or number, skip it
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Step 3: Compare the two characters (make them lowercase first)
            if s[left].lower() != s[right].lower():
                return False  # They don't match! Not a palindrome.
            
            # Step 4: Move both pointers inward to check the next characters
            left += 1
            right -= 1

        # If we made it through the whole string without hitting a mismatch
        return True
