import math

f = lambda x: math.pow(x,3)-1.7*math.pow(x,2)- 12.78*x -10.08 # funcao f

x0 = 4 # Chute inicial 1
x1 = 15 # Chute inicial 2
iteracoes = 5

for i in range(iteracoes):
  x2 = x1 - (f(x1)*(x1-x0))/(f(x1)-f(x0))
  x0 = x1
  x1 = x2
  
print("Raíz : ", x2)
