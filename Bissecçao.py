import math

def f(x): # Função do Exercício
  return math.pow(x,3)-1.7*math.pow(x,2)- 12.78*x -10.08 

a,b = -2,0 # Intervalo [a,b]
epsilon = 0.01 # [Condição de parada]

if (f(a)*f(b)<0): #Teorema de Bolzano
  while (math.fabs(b-a)/2 > epsilon):
    c = (a+b)/2 
    print(c)
    if f(c)==0:
      print("A raíz é ", c)
      break
    else:
      if f(a)*f(c) < 0:
        b = c
      else:
        a = c

  print("O valor da raíz é ", c)

else:
    print("Não há raíz neste intervalo")
