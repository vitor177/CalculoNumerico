import math

f = lambda x: math.pow(x,3)-1.7*math.pow(x,2)- 12.78*x -10.08 # funcao f

x0 = 4 # Chute inicial 1
x1 = 15 # Chute inicial 2
iteracoes = 6

for i in range(iteracoes):
  x2 = x1 - (f(x1)*(x1-x0))/(f(x1)-f(x0))
  x0 = x1
  x1 = x2
  if(f(x0)*f(x2) < 0):
      x0 = x0;
      x1 = x2;

  elif(f(x1)*f(x2) < 0):
      x0 = x2;
      x1 = x1;
  
print("Raíz : ", x2)
