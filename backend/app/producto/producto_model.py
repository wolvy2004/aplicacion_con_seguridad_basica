from ...database.conect_db import ConectDB
from ..marca.marca_model import MarcaModel as Marca

class ProductoModel():

    
    ## constructor
    def __init__(self, id:int=0, descripcion:str="", 
                 precio:float=0.0, stock:int=0, marca:Marca = None):
        self.id=id
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.marca = marca
        
        
        
    def serializar(self) -> dict:
        return {
            'id': self.id,
            'descripcion':self.descripcion,
            'precio':self.precio,
            'stock':self.stock,
            'marca':self.marca.serializar()
        }
    
    @staticmethod
    def deserializar(data:dict):
        return ProductoModel(
            id=data['id'], 
            descripcion=data['descripcion'],
            precio=data['precio'], 
            stock=data['stock'],
            marca=data['marca']            
        )
        
    
    """
    RECORDAR CERRAR LA CONEXION A LA BASE EN EL BLOQUE
    finally: 
        cnx.close()
    """
    @staticmethod
    def get_all():
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                # ejecuto la query
                cursor.execute(f"SELECT * FROM productos")
                # guardo en una variable el resultado
                rows = cursor.fetchall()
                # lista de diccionarios
                productos = []
                if rows:
                    for row in rows:
                        
                        marca = Marca.get_by_id(row['marca_id'])
                        row["marca"]=marca 
                        productos.append(row)
                    return productos                
                return False
            except Exception as exc:
                return {'mensaje': f" error al listar productos {exc}"}
            finally:
                cnx.close()
        
    def get_by_id(self):
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                # ejecuto la query
                cursor.execute("SELECT * FROM productos where id = %s", (self.id,))
                # guardo en una variable el resultado
                row = cursor.fetchone()
                if row:
                    marca = Marca.get_by_id(row['marca_id'])
                    row["marca"]=marca 
                    return row
                return False
            except Exception as exc:
                return {'mensaje':f" error buscar un producto {exc}"}
            finally:
                cnx.close()
                
    def create(self):
        cnx = ConectDB.get_connect()
        with cnx.cursor() as cursor:
            try:
                print(self.marca.id)
                # ejecuto la query
                cursor.execute("INSERT INTO productos (descripcion, precio, stock, marca_id) VALUES (%s,%s,%s,%s)", 
                               (self.descripcion, self.precio, self.stock, self.marca.id))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
                
            except Exception as exc:
                cnx.rollback()
                return {'mensaje':f" error buscar un producto {exc}"}
                
            finally:
                cnx.close()
        
    def update(self):
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                # ejecuto la query
                cursor.execute("UPDATE productos SET descripcion = %s, precio = %s, stock= %s, marca_id=%s where id=%s ", 
                               (self.descripcion, self.precio, self.stock, self.marca.id, self.id ))
                result = cursor.rowcount
                cnx.commit()
                
                if result > 0:
                    return True
                return False
                
            except Exception as exc:
                cnx.rollback()
                return {'mensaje':f" error modificar un producto {exc}"}
            finally:
                cnx.close()
                
    @staticmethod
    def delete(id:int):
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                # ejecuto la query
                cursor.execute("DELETE FROM productos where id = %s ", 
                               (id,))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {'mensaje':f" error buscar un producto {exc}"}
            finally:
                cnx.close()
    
    
    
    
    
    
    
    
    
      
    """ // metodos que la logica de la lectura esta en la clase conectar
        @staticmethod
        def get_all():
            sql = "SELECT * FROM productos"
            result = ConectDB.read(sql)
            productos =[]
            if result:
                for row in result:
                    productos.append(row)
            return productos
        
        def get_by_id(self):
            sql = "SELECT * FROM productos where id = %s"
            params = (self.id,)
            result = ConectDB.read(sql, params)
            return result if result else False
    """
 