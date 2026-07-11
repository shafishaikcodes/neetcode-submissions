from ctypes import c_int32

class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            partial_sum = c_int32(a ^ b).value
            carry = c_int32((a & b) << 1).value
            a = partial_sum
            b = carry

        return a