# To find the LENGTH of the Longest Substring without repeating characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # To find the max length of substring
        left = max_length = 0
        char_set = set()

        ## Sliding Window Technique
        for right in range(len(s)):
            while s[right] in char_set: ## to check if the character is repeating
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right]) ## to add the character if it is not repeating
            max_length = max(max_length, right - left + 1)

        return max_length                
