class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1   #是否进位
        for i in reversed(range(0, len(digits))):
            digit = (digits[i] + carry) % 10
            carry = 1 if digit < digits[i] else 0
            digits[i] = digit
        if carry == 1:
            return [1] + digits
        return digits

# Test
t = Solution()
print(t.plusOne([9]))
print(t.plusOne([4,3,2,1]))
print(t.plusOne([4,3,2,9]))
print(t.plusOne([4,9,9,9]))

