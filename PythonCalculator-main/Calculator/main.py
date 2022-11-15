## Author: Rui Santos
## Date : 15/11/2022
## Calculadora para ESA
from operator import pow, truediv, mul, add, sub, mod
from math import sqrt

##All the funcionalities that can be done by the calculator
operators = {
  '+%': None,
  '-%': None,
  'sqrt': sqrt,
  '+': add,
  '-': sub,
  '/': truediv,
  '%': mod,
  '**': pow,
  '*': mul
}

## Function to make the calculations
## S - Expression to calculate
def calculate(s):
    if s.isdigit():
        return float(s)
    for c in operators.keys():
        left, operator, right = s.partition(c)
        if operator == 'sqrt':
            return operators[operator](calculate(right))
        elif operator == '+%':
            if calculate(right) < 0:
                print('Erro! Percentagem negativa')
            else:
                return print("{:.2f}".format(round((100 + calculate(right))/100 * calculate(left), 0)))
        elif operator == '-%':
            if calculate(right) < 0:
                print('Erro! Percentagem negativa')
            else:
                return print("{:.2f}".format(round((calculate(left) - calculate(right)/100 * calculate(left)), 0)))
        elif operator in operators:
            return operators[operator](calculate(left), calculate(right))
    print('Erro! Não insira espaços no input!')
    exit()
print("Operações disponiveis \n+ soma \n- subtração \n/ divisão \n% resto \n** potência \nsqrt raiz quadrada "
     "\n-% retira uma determinada % a um valor \n+% adiciona uma determinada % a um vlor")
calc = input("Insira a conta a calcular:\n")
print(calculate(calc))




