def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        stack = []
        
        # recursively construct a tree of parentheses combinations
        def gen(open_cnt, close_cnt):
            if open_cnt == close_cnt == n:
                ans.append("".join(stack))
                return
            if open_cnt < n:
                stack.append("(")
                gen(open_cnt+1, close_cnt)
                stack.pop()
            if close_cnt < open_cnt:
                stack.append(")")
                gen(open_cnt, close_cnt+1)
                stack.pop()

        gen(0,0)
        return ans
