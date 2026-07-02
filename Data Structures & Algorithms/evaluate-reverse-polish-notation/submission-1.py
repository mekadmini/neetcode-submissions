class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack = [token] + stack
            else:
                operand_right = int(stack[0])
                operand_left = int(stack[1])
                match token:
                    case "+":
                        result = operand_right + operand_left
                    case "-":
                        result =  operand_left - operand_right
                    case "/":
                        result = operand_left / operand_right
                    case "*":
                        result = operand_right * operand_left
                stack = [result] + stack[2:]
        return int(stack[0])
