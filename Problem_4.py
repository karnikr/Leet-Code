# To find the Median of Two Sorted Arrays in O(log(m+n)) time
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # For this code to work, nums 1 has to be the smaller of the two arrays
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        # Finding the length of each array
        m, n = len(nums1), len(nums2)

        # For Binary Search
        start, end = 0, m
        s = m + n

        # Starting the Binary Search
        while start <= end:
            i = (start + end) // 2
            j = (m + n + 1) // 2 - i

            # Have to assign an intial value of negative inifity
            maxLHSi = float('-inf') if i == 0 else nums1[i-1]
            maxLHSj = float('-inf') if j == 0 else nums2[j-1]

            # Have to assign an initial value of infinity
            minRHSi = float('inf') if i == m else nums1[i]
            minRHSj = float('inf') if j == n else nums2[j]

            # These are the contraints as mentioned in the explanation notes
            if maxLHSi <= minRHSj and maxLHSj <= minRHSi:
                # if i is found
                # if the combined sorted array is even
                if s % 2 == 0:
                    return (max(maxLHSi,maxLHSj) + min(minRHSi,minRHSj)) / 2.0
                else:
                # if the combined sorted array is odd
                    return max(maxLHSi, maxLHSj)
            # if i is not found
            
            # if l1[i-1] > l2[j]
            elif maxLHSi > minRHSj:
                end = i - 1
            
            # if l2[j-1] > l1[i]
            else:
                start = i + 1
                
        raise ValueError("Input arrays are wrong")

