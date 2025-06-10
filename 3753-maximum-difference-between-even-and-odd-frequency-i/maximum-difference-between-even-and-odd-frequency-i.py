class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)

        odd_freq_chars = []
        even_freq_chars = []
        
        for char, count in freq.items():
            if count % 2 != 0:
                odd_freq_chars.append(count)
            else:
                even_freq_chars.append(count)
                
        if len(odd_freq_chars) == 0 or len(even_freq_chars) == 0:
            return -1
        
        max_odd = max(odd_freq_chars)
        min_even = min(even_freq_chars)
        
        return max_odd - min_even
            