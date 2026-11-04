# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
complex_number = complex(input())
r = complex_number.real
i = complex_number.imag
value_of_r = cmath.sqrt((r*r)+(i*i))
value_of_i = cmath.phase(complex(r,i))
print(value_of_r.real)
print(value_of_i)
