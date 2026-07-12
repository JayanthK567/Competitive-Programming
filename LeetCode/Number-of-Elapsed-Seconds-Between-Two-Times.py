class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        start = startTime.split(":")
        end = endTime.split(":")
        output = []
        for i in range(len(start)):
            output.append(int(end[i]) - int(start[i]))
        return (output[0]*60*60) + (output[1]*60) + output[2]