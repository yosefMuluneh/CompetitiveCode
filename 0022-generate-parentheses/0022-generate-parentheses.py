class Solution:
    def generateParenthesis(self,n):
        result = []
        self.backtrack("", 0, 0, n, result)
        return result


    def backtrack(self,curr, open_count, close_count, n, result):
        # Base case: if the current string is of length 2n, add it to the result
        if len(curr) == 2 * n:
            result.append(curr)
            return

        # Recursive cases:
        # Add an opening parenthesis if the count is less than n
        if open_count < n:
            self.backtrack(curr + "(", open_count + 1, close_count, n, result)

        # Add a closing parenthesis if the count of closing parentheses is less than the count of opening parentheses
        if close_count < open_count:
            self.backtrack(curr + ")", open_count, close_count + 1, n, result)