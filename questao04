import math
from math import e

def s(L):

  A = 8
  x1 = 20
  x2 = 30

  return 1/(math.sqrt(math.pow(x2,2)-math.pow(L,2))) + 1/(math.sqrt(math.pow(x1,2)-math.pow(L,2))) - 1/A


a,b = 10,18 # Intervalo [a,b]
epsilon = 0.00001 # [Condição de parada]
contador = 0


if (s(a)*s(b)<0): #Teorema de Bolzano
  while (math.fabs(b-a)/2 > epsilon):
    contador+=1
    c = (a+b)/2 
    if s(c)==0:
      print("A raíz é ", c)
      break
    else:
      if s(a)*s(c) < 0:
        b = c
      else:
        a = c

  print("O valor da raíz é ", c)

else:
    print("Não há raíz neste intervalo")

print("Número de iterações: ",contador)
