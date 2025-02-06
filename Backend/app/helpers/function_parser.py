import re
from sympy import diff
from math import sin, cos, tan, atan, acos, asin, pi, e, log, exp, pow

list_of_accepted_math_characters = ['+', '-', '*', '/', '**', '~', 'sin', 'cos', 'tan', 'cot', 'csc', 'sec', 'pi', 'e',
                                    'exp', 'ln', 'log', 'sqrt', '(', ')', 'x', 'math', '.', 'pow']

pattern = r'^(\+|\-|\*|\/|\**|~|x|math|.|sin|cos|tan|cot|csc|sec|pi|e|pow|exp|ln|log|sqrt|\(|\)|[0-9])+$'

sin = sin
cos = cos
tan = tan
sec = asin
csc = acos
cot = atan
pi = pi
e = e
exp = exp
ln = log
pow = pow

def is_valid_string(s) -> bool:
    return bool(re.fullmatch(pattern, s))

def string_function_evaluator(function_string, x) -> [float, ValueError]:
    x = x
    X = x
    if is_valid_string(function_string):
        try:
            return eval(function_string)
        except ValueError as error:
            return error
    else:
        print("invalid string formula")
        return 0

def string_function_differentiator(function_string:str) -> str:
    if is_valid_string(function_string):
        return str(diff(function_string))