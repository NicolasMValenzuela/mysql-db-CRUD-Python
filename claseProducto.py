import dbSQL

from sqlalchemy import Column, Integer, String, Float

class Producto(dbSQL.Base):
    __tablename__='producto'

    id = Column(Integer, primary_key= True)
    nombre = Column(String(length=50), nullable= False)
    precio = Column(Float)

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __repr__(self):
        return f'Producto ({self.nombre}, {self.precio})'

    def __str__(self):
        return self.nombre