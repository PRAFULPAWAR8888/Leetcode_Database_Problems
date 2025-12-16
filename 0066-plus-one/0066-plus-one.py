class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the last digit
        for i in range(len(digits)-1, -1,-1):

            # If the digits is less than 9, just add 1 and return
            if digits[i]<9:
                digits[i] += 1
                return digits
            
            # If digit is 9, make it 0 and carry continues
            digits[i] = 0
        #If all digits were 9, add a leading 1
        return [1] + digits
        