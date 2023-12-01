class Solution:
    def countAndSay(self, n: int) -> str:
     
        # Base case
        if n == 1:
            return "1"

        # Recursive case
        prev = self.countAndSay(n - 1)
        result = ""
        count = 1
        i = 0

        while i < len(prev):
            # Count the number of consecutive digits
            while i + 1 < len(prev) and prev[i] == prev[i + 1]:
                count += 1
                i += 1

            # Append the count and digit to the result
            result += str(count) + prev[i]

            # Reset the count
            count = 1
            i += 1

        return result