def put_producto():
    while True:
        try:
            producto_modificado = input('desea modificar algún producto? : S/N ').upper()
            assert producto_modificado == 'S' or producto_modificado == 'N'
            break
        except AssertionError:
            print('Debes ingresar S para modificar algún producto o N para dejar la lista igual \n')

print(put_producto())