class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        mid = []
        right = []
        for num in nums:
            if num < pivot:
                left.append(num)
            if num > pivot:
                right.append(num)
            if num == pivot:
                mid.append(num)
        return left + mid + right