class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [] #constructs one possibility with a list of parenths
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack)) #combines the stack characters
                return

            if openN < n:
                stack.append("(")
                backtrack(openN+1, closedN)
                stack.pop() #removes the last added "(" to find all possible combos

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        
        backtrack(0,0)
        return res