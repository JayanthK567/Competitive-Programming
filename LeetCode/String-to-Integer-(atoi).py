class Solution:
    def myAtoi(self, s: str) -> int:
        negative = False
        s = s.strip()
        digits = "1234567890"
        output = ""
        for i in range(len(s)):
            if i == 0 and (s[i] == '-' or s[i] == '+'):
                if s[i]== '-':
                    negative = True
                continue
            if s[i] in digits:
                output += s[i]
            else:
                break
        if output == '':
            return 0
        output = int(output)
        if negative: 
            output = output*(-1)
        if output > (2**31)-1:
            return (2**31)-1
        elif output < (2**31)*(-1):
            return (2**31)*(-1)
        else:
            return output