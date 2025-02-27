"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""

l = [1,0,1,1]

'''class Solution(object):
    def containsNearbyDuplicate(self, nums):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        new_list = {}
        i = 0
        prev_index = 0
        for index, n in enumerate(nums):
            if index > 0:
                prev_index = index - 1
            print(nums[index], nums[prev_index])'''

class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        
        d = {}

        for idx, x in enumerate(nums):
            if x in d and abs(idx - d[x] ) <= k:
                    #print(x, nums[idx], idx)
                    return True
            else:
                d[x] = idx
            print(d)
        return False

i = Solution().containsNearbyDuplicate(l, 1)
print(i)
#[1,2,3,1]