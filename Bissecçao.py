import math

f = lambda x: math.pow(x,3)-1.7*math.pow(x,2)- 12.78*x -10.08 # funcao f

a,b = 2,1000000 # Intervalo [a,b]
epsilon = 0.01 # [Condição de parada]
contador = 0

if (f(a)*f(b)<0): #Teorema de Bolzano
  while (math.fabs(b-a)/2 > epsilon):
    contador+=1
    c = (a+b)/2 
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

print("Número de iterações: ",contador)
