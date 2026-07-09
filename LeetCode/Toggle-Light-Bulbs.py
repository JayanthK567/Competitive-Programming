class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        output = set()
        for bulb in bulbs:
            if bulb not in output:
                output.add(bulb)
            else:
                output.remove(bulb)
        return sorted(output)