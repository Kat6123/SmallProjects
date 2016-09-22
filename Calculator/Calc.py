def number(list_):                          # List to number
    pow_ = 1
    n = 0
    list_.reverse()
    for _i in list_:
        n += _i * pow_
        pow_ *= 10
    return n


def calculate(op1, op2, act):               # Direct calculations
    if act == '+':
        return op1 + op2
    if act == '*':
        return op1 * op2
    if act == '/':
        return op1 / op2


def apply(symbol, _operand, _operator):     # Apply operator to operands in list
    if symbol == '-':                       # Support unary operation '-'
        n = _operand.pop()
        n = -n
        if not _operand:
            _operand.append(n)
            return
        if _operator and _operator.pop() == '(':
            _operator.append('(')
            _operand.append(n)
            return
        _operand.append(n)
        symbol = '+'
    _b = _operand.pop()
    _a = _operand.pop()
    _operand.append(calculate(_a, _b, symbol))


def add_operand(_num, _mid):
    if _mid:
        _num.append(number(_mid))
        _mid.clear()


def add_operator(symbol, _operator, _operand):
    prior = {'(': 0, '-': 1, '+': 1, '*': 2, '/': 2}
    if _operator:
        prev = _operator.pop()
        if prior.get(symbol) <= prior.get(prev):
            apply(prev, _operand, _operator)
        else:
            _operator.append(prev)
    _operator.append(symbol)


operand = []
operator = []
mid = []

while 1:
    expr = input("\n\nEnter expression:\nwithout spaces, enter = end\n")
    if not expr:
        break
    expr.strip()
    for i in expr:
        if '0' <= i <= '9':
            mid.append(int(i))
        elif i == '(':
            add_operand(operand, mid)
            operator.append(i)
        elif i == ')':
            if operator.count('(') == 0 or not operator:
                print("Invalid expression!")
                break
            add_operand(operand, mid)
            while 1:
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
