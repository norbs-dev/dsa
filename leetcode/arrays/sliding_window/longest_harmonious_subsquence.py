class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        lenght = 0
        for n in range(len(nums)):
            d[nums[n]] = d.get(nums[n], 0) + 1
        for i in d:
            if i +1 in d:
                lenght = max(lenght, d[i] + d[i+1])
        return lenght
            

l = [1,2,3,4]
i = Solution().findLHS(l)
print(i)
        