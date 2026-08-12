## AVALIAÇÃO 1 - QUESTÃO 3

## Função que calcula MP
def MediasProva(a, b):
  media = (a + b)/2
  print(f"MEDIA DAS PROVAS (MP): {media}")
  return media

## Função que calcula MT
def MediasTrabalho(a, b):
  media = (a + b)/2
  print(f"MEDIA DOS TRABALHOS (MT): {media}")
  return media

## Função que calcula MF
def MediaFinal(a, b):
  media = (0.6*a) + (0.4*b) 
  print(f"MEDIA FINAL (MF): {media}")
  return media

## Função que verifica condição de aprovação
def VerificaNota(n):
  if  10 >= n >= 6:
    return print(f"Nota: {n}, APROVADO!")
  else:
    return print(f"Nota: {n}, REPROVADO!")
    
while(True):

  ## Entrada de valores
  p1 = float(input("DIGITE A NOTA DA PROVA 1: "))
  p2 = float(input("DIGITE A NOTA DA PROVA 2: "))
  t1 = float(input("DIGITE A NOTA DA TRABALHO 1: "))
  t2 = float(input("DIGITE A NOTA DA TRABALHO 2: "))

  ## Verificação de notas válidas
  if (10 >= p1 >= 0) and (10 >= p2 >= 0) and (10 >= t1 >= 0) and (10 >= t2 >= 0):
    print("NOTAS VÁLIDAS\n")
    break
  else:
    print("NOTAS INVÁLIDAS, TENTE NOVAMENTE COM VALORES ENTRE 0 E 10")


## Requisições  
MP = MediasProva(p1, p2)
MT = MediasTrabalho(t1, t2)
MF = MediaFinal(MP, MT)
VerificaNota(MF)
