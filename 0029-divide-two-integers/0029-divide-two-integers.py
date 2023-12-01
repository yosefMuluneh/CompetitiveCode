class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        negative = (dividend < 0) != (divisor < 0)

        # Convert dividend and divisor to positive
        dividend = abs(dividend)
        divisor = abs(divisor)

        # Initialize the quotient and the current divisor
        quotient = 0
        current_divisor = divisor

        # Binary search-like algorithm
        while dividend >= current_divisor:
            # Find the largest multiple of the current divisor that is still smaller or equal to the dividend
            multiple = 1
            while (current_divisor << 1) <= dividend:
                current_divisor <<= 1
                multiple <<= 1

            # Subtract the multiple of the divisor from the dividend
            dividend -= current_divisor

            # Add the multiple to the quotient
            quotient += multiple

            # Reset the current divisor to the original divisor
            current_divisor = divisor

        # Adjust the sign of the quotient
        if negative:
            quotient = -quotient

        return quotient