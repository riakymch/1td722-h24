import math
from tokenize import TokenError
# from MA2tokenizer import TokenizeWrapper

"""
Interface class to the tokenizer module.
"""
import io
import tokenize

INIT_FILE = 'MA2init.txt'


class TokenizeWrapper:
    def __init__(self, line):
        self.line = line
        self.tokens = tokenize.generate_tokens(io.StringIO(line).readline)
        self.current = next(self.tokens)
        self.previous = 'START'

    def __str__(self):
        return self.current[0] + self.current[1]

    def get_current(self):
        if self.current[0] > 0:
            return self.current[1]
        else:
            return 'NO MORE TOKENS'

    def get_previous(self):
        return self.previous

    def next(self):
        # The return value is mainly intended for debugging purposes
        if self.has_next():
            self.previous = self.current[1]
            self.current = next(self.tokens)
            # print('next', self.current[0], self.current[1])
            return self.current
        else:
            return (0, 'EOS')

    def is_number(self):
        return self.current[0] == 2

    def is_name(self):
        return self.current[0] == 1

    def is_string(self):
        return self.current[0] == 3

    def is_newline(self):
        return self.current[0] == 4

    def is_comment(self):
        return self.current[0] == 55

    def is_at_end(self):
        return self.current[0] == 0 or self.current[0] == 4 or \
            self.current[1][0] == '#'
        # self.current[0] == 55   # This test doesn't work everywhere
        # try to check on '#' instead

    def has_next(self):
        return self.current[0] != 0 and self.current[0] != 4


def my_log(arg):
    return math.log(arg)


def fac(n):
    if int(n) != n or n < 0:
        raise EvaluationError(f"Argument to fac is {n}. Must be integer >= 0")
    res = 1
    for i in range(1, int(n)+1):
        res *= i
    return res


def fib(n):
    if int(n) != n or n < 0:
        raise EvaluationError(f"Argument to fib is {n}. Must be integer >= 0")
    f0, f1 = 0, 1
    while n > 0:
        f0, f1 = f1, f0 + f1
        n -= 1
    return f0


FUNCTIONS_1 = {  # Functions with a single argument
    'sin': math.sin,
    'cos': math.cos,
    'exp': math.exp,
    'log': my_log,
    'fac': fac,
    'fib': fib,
}

FUNCTIONS_N = {  # Functions with several arguments
    'sum': sum,
    'max': max,
    'min': min
}


class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


def statement(wtok, variables):
    """ See syntax diagram for statement"""
    try:
        result = assignment(wtok, variables)
    except TypeError as te:
        raise EvaluationError(te)
    if wtok.is_at_end() == False:
        raise SyntaxError('Expected end of line')
    return result


def assignment(wtok, variables):
    """ See syntax diagram for assignment"""
    result = expression(wtok, variables)
    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_name():
            variables[wtok.get_current()] = result
            wtok.next()
        else:
            raise SyntaxError("Expected name after '=' ")
    return result


def expression(wtok, variables):
    """ See syntax diagram for expression"""
    result = term(wtok, variables)
    while wtok.get_current() in ('+', '-'):
        if wtok.get_current() == '+':
            wtok.next()
            result = result + term(wtok, variables)
        else:
            wtok.next()
            result = result - term(wtok, variables)
    return result


def term(wtok, variables):
    """ See syntax diagram for term"""
    result = factor(wtok, variables)
    while wtok.get_current() == '*':
        wtok.next()
        result = result * factor(wtok, variables)
    return result


def factor(wtok, variables):
    """ See syntax diagram for factor"""
    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()

    elif wtok.get_current() in FUNCTIONS_1:
        func = wtok.get_current()
        wtok.next()
        if wtok.get_current() == '(':
            result = FUNCTIONS_1[func](factor(wtok, variables))
        else:
            raise SyntaxError("Expected '(' after function name")

    elif wtok.get_current() in FUNCTIONS_N:
        func = wtok.get_current()
        wtok.next()
        args = arglist(wtok, variables)
        result = FUNCTIONS_N[func](args)

    elif wtok.is_name():
        if wtok.get_current() in variables:
            result = variables[wtok.get_current()]
            wtok.next()
        else:
            raise EvaluationError(
                f"Undefined variable: '{wtok.get_current()}'")

    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()

    elif wtok.get_current() == '-':
        wtok.next()
        result = -factor(wtok, variables)

    else:
        raise SyntaxError(
            "Expected number, word or '('")

    return result


def arglist(wtok, variables):  # A5
    """ See syntax diagram for arglist"""

    return [99]  # Just a dummy value. Should be changed.


def vars_print(variables):
    for name, value in sorted(variables.items()):
        print(f"   {name:<5} : {value}")


def calculator():
    """
    Handles:
       the iteration over input lines,
       the commands 'quit' and 'vars' and
       catches raised exceptions.
    Starts with reading the init file
    """

    print("\n\nM2: Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}

    lines_from_file = ''
    try:
        with open(INIT_FILE, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            if line != '':
                print('\ninit  :', line)
            else:
                print()
        else:
            line = input('\nInput : ')
        if line == '' or line[0] == '#':
            continue
        wtok = TokenizeWrapper(line)
        if wtok.get_current() == 'vars':
            vars_print(variables)
        elif wtok.get_current() in ('quit', 'q', 'exit'):
            print('Bye')
            return
        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                if type(result) == str:
                    print(f"Result: '{result}'")
                else:
                    print('Result:', result)

            except EvaluationError as ee:
                print("*** Evaluation error:", ee)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                    f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')


if __name__ == "__main__":
    calculator()
