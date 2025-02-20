"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "Mr Ding"
Output: "rM gniD"
 

Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
"""

class Solution(object):
    def reverseWords(self, s):
        words_list = s.split()
        reversed_word = ''
        for word in words_list:
            reversed_s_word = self.reverse(word)
            reversed_word += reversed_s_word + " "
        return reversed_word.strip()


    def reverse(self, word):
        reversed_word = ''
        chars = [char for char in word]
        for _ in range(len(chars)):
            reversed_word += chars.pop()
        return reversed_word

i = Solution().reverseWords("Let's take LeetCode contest")                
print(i)
