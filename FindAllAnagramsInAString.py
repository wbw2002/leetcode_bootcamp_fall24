"""
Given two strings s and p, return an array of all the start indices of p's 
anagrams in s. You may return the answer in any order.
"""

from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # Length of the two strings
        len_s, len_p = len(s), len(p)
        
        # Edge case: if p is longer than s, return an empty list
        if len_p > len_s:
            return []
        
        # Frequency counters for p and the current window in s
        p_count = Counter(p)
        s_count = Counter()
        
        # Result list to store the starting indices
        result = []
        
        # Sliding window approach
        for i in range(len_s):
            # Add the current character to the s_count
            s_count[s[i]] += 1
            
            # Remove the character that is out of the current window
            if i >= len_p:
                if s_count[s[i - len_p]] == 1:
                    del s_count[s[i - len_p]]
                else:
                    s_count[s[i - len_p]] -= 1
            
            # Compare the two counters
            if s_count == p_count:
                result.append(i - len_p + 1)
        
        return result
