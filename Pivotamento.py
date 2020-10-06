import math

matriz = []

with open(f'm3.txt', 'r') as f:
    n = int(f.readline())
    matriz = [[float(num) for num in line.split(' ')] for line in f]
b = []
A = []
for i in matriz:  # Extrair a matriz b do conjunto de dados
    b.append(i[-1])
aux = int(n)
for i in reversed(matriz): # Extrair a matriz A do conjunto de dados
    del i[aux]

A = matriz

def gaussPivoteamento(A,b):
  # acessar as linhas da matriz
  for i in range(len(A)):
    # verificar qual o maior pivô
    pivo = math.fabs(A[i][i])
    linhaPivo = i

    for j in range(i+1, len(A)):
      if math.fabs(A[j][i] > pivo):
        pivo = math.fabs(A[j][i])
        linhaPivo = j

    # permutar as linhas
    if linhaPivo != i:
      linhaAuxiliar = A[i]
      A[i] = A[linhaPivo]
      A[linhaPivo] = linhaAuxiliar

      bAuxiliar = b[i]
      b[i] = b[linhaPivo]
      b[linhaPivo] = bAuxiliar

      # eliminação gaussiana
    for m in range(i+1, len(A)):
      multiplicador = A[m][i]/A[i][i]
      for n in range(i, len(A)):
        A[m][n] -= multiplicador*A[i][n]
      b[m] -= multiplicador*b[i]

  vetorSolucao = []
  for i in range(len(A)):
    vetorSolucao.append(0)
  linha = len(A) - 1
  while linha >= 0:
    x = b[linha]
    coluna = len(A) - 1
    while coluna > linha:
      x -= A[linha][coluna] * vetorSolucao[coluna]
      coluna -= 1
    x /= A[linha][linha]
    linha -= 1
    vetorSolucao[coluna] = x
  print(vetorSolucao)
  return vetorSolucao


def obterNorma(b, A, vetorSolucao):
    value = 0
    Ax = []
    for i in range(len(vetorSolucao)):
        value = 0
        for j in range(len(vetorSolucao)):
            value += vetorSolucao[j] * A[i][j]
        Ax.append(value)

    res = []
    for i in range(len(vetorSolucao)):
        aux = b[i] - Ax[i]
        res.append(aux)

    norma = 0
    for i in range(len(vetorSolucao)):
        norma += pow(res[i], 2)
    return pow(norma, 0.5)


gaussPivoteamento(A,b)

obterNorma(b,A,gaussPivoteamento(A,b))

