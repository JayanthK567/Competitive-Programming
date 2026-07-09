class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score = 0
        counter = 0
        digits = {'0','1','2','3','4','5','6','7','8','9'}
        for point in events:
            if point in digits:
                score += int(point)
            elif point == 'W':
                counter += 1
            else:
                score += 1

            if counter == 10:
                return [score,counter]
        return [score,counter]