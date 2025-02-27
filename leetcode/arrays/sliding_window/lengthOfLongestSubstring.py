# set
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = max_lenght = 0
        char_set = set()

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])
            max_lenght = max(max_lenght, right - left + 1)
        print(char_set)
        return max_lenght
        

#hash map
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        count = {}
        left = _max = 0
        for right, c in enumerate(s):
            count[c] = 1 + count.get(c, 0)
            while count[c] > 1:
                count[s[left]] -= 1
                left += 1

            _max = max(_max, right - left + 1)
        return _max

i = Solution().lengthOfLongestSubstring('pwwkew')
print(i)