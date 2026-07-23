class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        volume = length * width*height


        bulky =(
            length >=10000 or
            width >= 10000 or
            height >= 10000 or
            volume >= 1000000000
        )

        heavy = mass >= 100

        if bulky and heavy :
            return "Both"
        elif bulky :
            return "Bulky"
        elif heavy :
            return "Heavy"
        else :
            return "Neither"