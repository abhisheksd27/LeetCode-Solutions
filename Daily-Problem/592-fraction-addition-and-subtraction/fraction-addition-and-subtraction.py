class Solution:
    def fractionAddition(self, expression: str) -> str:

        numerator = 0
        denominator = 2520

        for frac in expression.split("+"):
            for j, f in enumerate(frac.split("-")):
                if f == "":
                    continue
                n, d = [int(v) for v in f.split("/")]
                if j == 0:
                    numerator += denominator // d * n
                else:
                    numerator -= denominator // d * n


        if numerator == 0:
            return "0/1"
        
        for factor in (2, 3, 5, 7):
            while (numerator % factor == 0) and (denominator % factor == 0):
                numerator //= factor
                denominator //= factor

        return f"{numerator}/{denominator}"
        

        

        