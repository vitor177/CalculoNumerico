import math
from math import e

def s(t):

  s0 = 300
  m = 0.25
  k = 0.1
  g = 32.17
  return s0 - ((m*g)/k)*t + ((math.pow(m,2)*g)/(math.pow(k,2)))*(1-math.pow(e,(-k*t)/m))

x0 = 1 # Chute inicial 1
x1 = 20 # Chute inicial 2
iteracoes = 4
contador = 0
for i in range(iteracoes):

  contador+=1
  x2 = x1 - (s(x1)*(x1-x0))/(s(x1)-s(x0))
  x0 = x1
  x1 = x2
  if (abs(s(x2)<0.00001)):
    print(x2)
  
print("Raíz : ", x2)
print(contador)
