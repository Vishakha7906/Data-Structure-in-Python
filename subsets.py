class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        if n==0:
            return res
        
        for i in range(pow(2, n)):
            l = []
            for j in range(n):
                if i & (1 << j) > 0:
                    l.append(nums[j])
            res.append(l)
        return res
                
        