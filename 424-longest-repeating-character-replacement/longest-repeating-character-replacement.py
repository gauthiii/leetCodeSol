class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}
        left = 0
        max_frequency = 0
        max_length = 0

        for right in range(len(s)):
            # Add current character to window
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            
            # Update max frequency in current window
            max_frequency = max(max_frequency, char_count[s[right]])
            
            # Current window size
            window_length = right - left + 1
            
            # If we need more than k replacements, shrink window
            if window_length - max_frequency > k:
                char_count[s[left]] -= 1
                left += 1
            
            # Update max length
            max_length = max(max_length, right - left + 1)
        
        return max_length
        