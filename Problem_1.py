## This is my solution for the Two Sum Problem

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i in range(0,len(nums)):
            for j in range(1,len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    if i not in result:
                        result.append(i)
                    if j not in result:
                        result.append(j)
        
        return result