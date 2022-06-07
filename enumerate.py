'''
Existem algumas maneiras de imprimir de mostrar o numero do item e o seu respectivo indice, uma delas é usando for e len:
'''

lista=["abacate", "bola", "cachorro"]
for i in range(len(lista)):
  print(i, lista[i])

'''
A outra maneira é usando a função ENUMERATE, pois acaba facilitando usar esta função, especilamente quando o código é grande. 
Onde ela retorna no i a (posição que está dentro da lista, 0, 1, 2 e etc) e no nome retorna o que esta “escrito” naquela posição (abacate, bola, cachorro).
'''

lista=["abacate", "bola", "cachorro"]
for i, nome in enumerate(lista):
  print(i, nome)
