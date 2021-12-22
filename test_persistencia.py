"""
Pruebas persistencia.
"""
from persistencia import guardar_pedido

def test_guardar_pedido():
    """
    prueba general
    """
    with open("pedidos.txt", "w+", encoding="utf-8") as file:
        guardar_pedido("Victor", "Hernández")
        guardar_pedido("Michael", "Jordan")
        firstline = file.readline()
        secondline = file.readline()
        file.close()
    assert firstline == "-Victor Hernández\n"
    assert secondline == "-Michael Jordan\n"
