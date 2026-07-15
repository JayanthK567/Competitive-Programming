class Solution:
    def maxArea(self, height: List[int]) -> int:
        largest = 0
        left = 0
        right = len(height)-1
        while left < right:
            largest = max(min(height[left],height[right]) * (right - left), largest)

            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return largest