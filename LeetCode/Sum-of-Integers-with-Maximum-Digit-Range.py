class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        maxRange = 0
        data = {}
        output = 0
        for num in nums:
            duplicate = num #duplicate value copy
            if num ==0:
                continue 
            largest = 0
            smallest = 10
            while num > 0:
                largest = max(largest,num%10)
                smallest = min(smallest,num%10)
                num = num //10
            ranged = largest-smallest
            data[duplicate] = ranged
            maxRange = max(maxRange,ranged)
        for num in nums:
            if data[num] == maxRange:
                output += num
        return output

