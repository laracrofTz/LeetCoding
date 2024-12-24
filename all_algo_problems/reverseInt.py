# Given a signed 32 bit integer, x return x with its digits reversed
# If reversing the digits causes x to go out of the signed 32 bit integer range --> [-2^31 to 2^32-1] return 0
# Assume env does not allow you to store 64 bit int signed or unsigned

# Possible question or assumptions
# 

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_str = str(abs(x))
        reverse_x = int(x_str[::-1]) # reversing the string depends on the length of the string, hence will be O(n)
        if reverse_x < (2**31)-1 or (reverse_x*-1) > -2**31:
            if x < 0:
                return reverse_x * -1
            return reverse_x
        else: return 0


# Complexity
# Time complexity is O(n) due to string reversal
# Space complexity is O(n) since the result returned is dependent on the length of the int parsed as string