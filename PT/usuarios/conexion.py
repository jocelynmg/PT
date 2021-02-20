import mysql.connector

def connectarBD():
    """Esta función se utiliza para crear la conexión con la BD"""
    
    database = mysql.connector.connect(
        host = 'localhost',
        user = 'admin',
        passwd = 'secreto',
        database = 'pi_docker'
    )

    cursor = database.cursor(buffered=True)

    return [database, cursor]