class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) <=1:
            return False

        for b in s: 
            if b in "({[":
                stack.append(b)
            else:
                if len(stack) == 0:
                    return False

                opp = stack.pop()
                match opp:
                    case '(':
                        if b != ')':
                            return False
                    case '[':
                        if b != ']':
                            return False
                    case '{':
                        if b != '}':
                            return False
        return not stack