
listaMerca= []

def engadirProduto(lmerca):
  produto = input("Que produto quere mercar?")
  lmerca.append(produto)
  print("Produto engadido")


def eliminarProduto(lmerca):
  produto= input("Que produto quere eliminar?")
  if produto in lmerca:
      lmerca.remove(produto)
  print("Produto eliminado")



def amosarLista(lmerca):
    print("Os produtos da lista son:")
    for produto in lmerca:
      print(produto)


def menuPrincipal():
    opcion= 0
    listaDeLaCompra=[]
    while opcion != 4:
        print("Opcions")
        print("1. Engadir produto")
        print("2. Eliminar produto")
        print("3. Amosar lista ")
        print("4. Sair")
        opcion= int(input("Ingresa una opcion: "))
        if opcion == 1:
            produtoAgregado= input("Que produto queres agregar: ")
            listaDeLaCompra.append(produtoAgregado)
        if opcion == 2:
            print("Productos: ", listaDeLaCompra)
            produtoEliminado= input("Que produto queres eliminar: ",)
            listaDeLaCompra.remove(produtoEliminado)
            print("Produto elimado")
        if opcion == 3:
            print("Lista: ",listaDeLaCompra)
    print("Grazas pola tua compra")

