class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #ord1 = 49
        if num1 == "0" or num2 == "0":
            return "0"
        
        val1 = 0
        val2 = 0
        
        for num in num1:
            val1 = (val1*10) + (ord(num)-48)
        
        for num in num2:
            val2 = (val2*10) + (ord(num)-48)
        
        return str(val1*val2)