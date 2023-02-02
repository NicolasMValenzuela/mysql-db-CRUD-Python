import dbSQL
from claseProducto import Producto
from sqlalchemy import update
from random import *
from prettytable import PrettyTable

def data():
    return randint(0,1000), randint(0,3) 


def post_producto(cantidad_de_productos = int(input('Ingrese la cantidad de productos que quiere agregar a la lista: '))):
    counter = 0
    lista_productos = ['carne', 'huevos', 'leche', 'queso']
    while True:
        try:   
            for i in range(counter, cantidad_de_productos):
                precio, nombre = data()
                producto = Producto(nombre = lista_productos[nombre], precio = precio)
                dbSQL.Session.add(producto)
                dbSQL.Session.commit()
                counter +=1
            print('Productos agregados exitosamente')
            break
        except ValueError:
            print('uno de los valores no fue ingresado correctamente')
            continue

def get_producto():
    tabla = PrettyTable(['id', 'nombre', 'precio'])
    filtro = input('ingrese el producto a buscar o deje la entrada vacia para ver la lista completa: ')
    if filtro != '':
        consulta = dbSQL.Session.query(Producto).filter_by(nombre = filtro).all()
        print(consulta)
    else:
        consulta = dbSQL.Session.query(Producto).all()
        for producto in consulta:
            tabla.add_row([producto.id, producto.nombre, producto.precio])
        print (tabla)

def put_producto():
    while True:
        try:
            lista_ids= []
            tabla = PrettyTable(['id', 'nombre', 'precio'])
            choice  = input('desea modificar algún producto? : S/N ').upper()
            assert choice   == 'S' or choice  == 'N'
            break
        except AssertionError:
            print('Debes ingresar S para modificar algún producto o N para dejar la lista igual \n')
        
    if choice == 'S':
        lista_productos = dbSQL.Session.query(Producto).all()
        for producto in lista_productos:
            tabla.add_row([producto.id, producto.nombre, producto.precio])
        print (tabla)
        producto_nuevo = input('ingrese el producto a cambiar: \n')
        precio_nuevo = int(input('ingrese el precio nuevo: '))

        productos_a_modificar = [producto for producto in lista_productos if producto.nombre == producto_nuevo]

        print('ID de los elementos a modificar: \n')
        for i in range (len(productos_a_modificar)):
            lista_ids.append(productos_a_modificar[i].id)
            print(f'ID: {productos_a_modificar[i].id}')

        for i in range(len(lista_productos)):
            if producto_nuevo == lista_productos[i].nombre:
                
                id = int(input('Elija el ID del elemento a modificar: '))
                while id not in lista_ids:
                    id = int(input('ERROR_ID_INCORRECTO: Elija el ID del elemento a modificar: '))

                consulta = update(Producto).where(Producto.id == id).values(precio= precio_nuevo)
                dbSQL.Session.execute(consulta)
                dbSQL.Session.commit()
        
                continue_choice = input("Deseas modificar otro producto?: S/N ").upper()
                if continue_choice == 'N':
                    break

        

def delete_producto():
    while True:
            try:
                tabla = PrettyTable(['id', 'nombre', 'precio'])
                lista_ids = []
                choice = input('Deseas eliminar algún producto ? : S/N ').upper()
                assert choice == 'S' or choice == 'N'
                if choice == 'N':
                    break

                lista_productos = dbSQL.Session.query(Producto).all()
                for producto in lista_productos:
                    tabla.add_row([producto.id, producto.nombre, producto.precio])
                print (tabla)

                producto_borrado = input('ingrese el nombre del producto a eliminar: ')
                
                productos_a_eliminar = [producto for producto in lista_productos if producto.nombre == producto_borrado]
                
                print(len(productos_a_eliminar))    
                while len(productos_a_eliminar) == 0:
                    try:
                        choice2 = input('No se encuentra el elemento a eliminar, desea eliminar algún producto ?: S/N \n').upper()
                        assert choice2 == 'S' or choice2 == 'N'
                        if choice2 == 'S':
                            producto_borrado = input('ingrese el nombre del producto a eliminar: ')
                        
                            productos_a_eliminar = [producto for producto in lista_productos if producto.nombre == producto_borrado]
                        else:
                            break
                    except AssertionError:
                        print('Error debes elegir entre S o N')
                        choice2 = input('No se encuentra el elemento a eliminar, desea eliminar algún producto ?: S/N \n').upper()

                print('ID de los elementos a eliminar: \n')
                for i in range (len(productos_a_eliminar)):
                    lista_ids.append(productos_a_eliminar[i].id)
                    print(f'ID: {productos_a_eliminar[i].id}')

                for i in range(len(lista_productos)):
                    if producto_borrado == lista_productos[i].nombre:
                        
                        id = int(input('Elija el ID del elemento a eliminar: '))
                        while id not in lista_ids:
                            id = int(input('ERROR_ID_INCORRECTO: Elija el ID del elemento a eliminar: '))
                        producto = dbSQL.Session.query(Producto).filter_by(id = id).first()
                        dbSQL.Session.delete(producto)
                        dbSQL.Session.commit()
                
                        continue_choice = input("Deseas eliminar otra entrada del mismo producto?: S/N ").upper()
                        if continue_choice == 'N':
                            break

            except AssertionError:
                print('debes elegir una letra entre S, para decir si o N para decir no')


    lista_final = dbSQL.Session.query(Producto).all()
    
    for producto in lista_final:
            tabla.add_row([producto.id, producto.nombre, producto.precio])
    print (tabla)
    
def run():
    post_producto()
    get_producto()
    put_producto()
    delete_producto()

if __name__== '__main__':
    dbSQL.Base.metadata.create_all(dbSQL.engine)
    run()