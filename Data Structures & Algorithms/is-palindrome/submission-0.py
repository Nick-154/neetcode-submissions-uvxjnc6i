class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            # Move left pointer forward until we find an alphanumeric char
            while left < right and not s[left].isalnum():
                left += 1
            
            # Move right pointer backward until we find an alphanumeric char
            while right > left and not s[right].isalnum():
                right -= 1
            
            # Compare characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False
            
            # After a successful match, shift both pointers inward
            left += 1
            right -= 1
            
        return True