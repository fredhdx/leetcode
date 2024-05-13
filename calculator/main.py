class Solution:
    def division(self, a, b):
        return -(-a // b) if (a < 0) ^ (b < 0) else a // b
    def calculate(self, s: str) -> int:
        stack = []
        prev_op, num = "+", 0
        
        def calc(op, v):
            if op == "+":
                stack.append(v)
            elif op == "-":
                stack.append(-v)
            elif op == "*":
                stack.append(stack.pop(-1) * v)
            else:
                stack.append(self.division(stack.pop(-1), v)) 
        
        for c in (s+"@"):
            if c == " ":
                continue
            elif c.isdigit():
                num = num*10 + int(c)
            elif c in "+-*/@":
                calc(prev_op, num)
                num = 0
                prev_op = c
            elif c in "(":
                # .....-10/2x(
                # prev_op = x, store it for recovery
                # set num=0, prev_op=+ for calc within bracket
                stack.append(prev_op)
                prev_op = "+"
                # num = 0
            elif c in ")":
                # .....+2x8/2), finish last (op, v) pair within
                calc(prev_op, num)
                # [...20, +, -23, 2x8/2, ]
                tmp = stack.pop(-1)
                num = 0
                while type(tmp) == int:
                    num += tmp
                    tmp = stack.pop(-1)
                # num: result from (). tmp: prev_op before ()
                prev_op = tmp
                # num, prev_op => bracket result, bracket prev op
                # ....) + 
                # for any operation right after bracket, bracket result will be treated as normal (op, v) pair and put to stack
            
        return sum(stack)


# test
def run_test(testcase, ans=0, i=0):
    sol = Solution()
    result = sol.calculate(testcase)
    print(f"Case{i}: ", testcase)
    print("Passed" if ans == result else "Failed")
    print(f"Res: {result}, Ans: {ans}")

    return ans == result

testcases = [
    ["2*(5+5*2)/3+(6/2+8)", 21],
    ["1+3+5/23-(23-10*29)", 271],
    ["-(2+6* 3+5- (3*14/7+2)*5)+3", 18],
    ["-(1+(1+2+(10+2)*5)+((((1)+1)+1)+1))", -68]
]

print('==== Running Test Cases ====\n')
success = 0
for i, (case, ans) in enumerate(testcases):
    if run_test(case, ans, i):
        success += 1
    print()

n = len(testcases)
print(f"Success: {success}/{n}, Failed: {n-success}/{n}")
print('==== END ====')