"""
Author=Rabi
Int, Float, Complex ,
Numbers are very fundamental or simple data type but they can be complex datatype
"""
# int
num = 34
print(f'num={num}')
#Float
num = 3.14
print(f'num= {num}')
import sys # It allow us to take other ppl code.
print(sys.float_info)  # Official todument find from python document and number is generating
#Complex
num = 3 +6j
print(f'num = {num}')
num = complex(5,3) # Complex number define in two real and imaginary number as seen
print(f'num = {num}')
print(f'real = {num.real}, imag = {num.imag}')

# Basic Numberic operator
x = 3
print(f'x = {x}')
y = x+3 # Add
print(f'add = {y}')
y = x-1 # Substract
print(f'Substract = {y}')
y = x*5.23 # Multiple
print(f'Multiple = {y}')
y = x/0.2 # Divide
print(f'Divide = {y}')
y = x**2 # Pow
print(f'Pow = {y}')
y = x%2.5 # Remain
print(f'Remain = {y}')