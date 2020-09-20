import math

f = lambda x: math.pow(x,3)-1.7*math.pow(x,2)- 12.78*x -10.08 # funcao f

d_fun = lambda x: (f(x+1e-5)-f(x))/1e-5 # calculando derivada de f

x = 4 # Chute inicial 
iteracoes = 5 # quantidade de iteracoes ate convergir

for i in range(iteracoes):
  x = x - f(x)/(d_fun(x)) # iteração pelo método de newton

print("Raíz : ", x)

