"""
Leetcode #75

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        red = -1
        blue = len(nums)
        pointer = 0

        while pointer < blue:
            if nums[pointer] == 0:
                nums[pointer], nums[red + 1] = nums[red + 1], nums[pointer]
                red += 1
                pointer += 1
            elif nums[pointer] == 2:
                nums[pointer], nums[blue - 1] = nums[blue - 1], nums[pointer]
                blue -= 1
            else:
                pointer += 1
        return nums
