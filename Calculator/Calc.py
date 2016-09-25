def number(list_):                      # List to number
    pow_ = 1
    n = 0
    list_.reverse()
    for i in list_:
        n += i * pow_
        pow_ *= 10
    return n


def calculate(op1, op2, act):           # Direct calculations
    if act == '-':
        return op1 - op2
    if act == '+':
        return op1 + op2
    if act == '*':
        return op1 * op2
    if act == '/':
        try:
            n = op1 / op2
        except ZeroDivisionError:
            print("Division by zero!")
            main()
        else:
            return n


def apply(symbol, operand, operator):  # Apply operator to operands in list
    if symbol == '_':                    # '_' support unary minus
        n = operand.pop()
        n = -n
        operand.append(n)
    else:
        b = operand.pop()
        a = operand.pop()
        operand.append(calculate(a, b, symbol))


def add_operand(num, mid):
    if mid:
        num.append(number(mid))
        mid.clear()


def add_operator(symbol, operator, operand):
    prior = {'(': 0, '-': 1, '+': 1, '*': 2, '/': 2, '_': 3}
    if operator:
        prev = operator.pop()
        if prior.get(symbol) <= prior.get(prev):
            apply(prev, operand, operator)
        else:
            operator.append(prev)
    operator.append(symbol)


def main():
    operand = []
    operator = []
    mid = []

    while True:
        expr = input("\n\nEnter expression:\nwithout spaces, enter = end\n")
        if not expr:
            break
        sign = True
        for i in expr:
            if '0' <= i <= '9':
                sign = False
                mid.append(int(i))
            elif i == '(':
                sign = True
                add_operand(operand, mid)
                operator.append(i)
            elif i == ')':
                if operator.count('(') == 0 or not operator:
                    print("Invalid expression!")
                    break
                add_operand(operand, mid)
                while True:
                    ch = operator.pop()
                    if ch == '(':
                        break
                    else:
                        apply(ch, operand, operator)
            elif i == '+':
                add_operand(operand, mid)
                add_operator('+', operator, operand)
            elif i == '-':
                add_operand(operand, mid)
                if sign:
                    add_operator('_', operator, operand)
                    sign = False
                else:
                    add_operator('-', operator, operand)
            elif i == '*':
                add_operand(operand, mid)
                add_operator('*', operator, operand)
            elif i == '/':
                add_operand(operand, mid)
                add_operator('/', operator, operand)
            else:
                print("Invalid expression!")
                break
        else:
            add_operand(operand, mid)
            while operator:
                ch = operator.pop()
                apply(ch, operand, operator)
            print("Result: ", operand.pop())

main()
