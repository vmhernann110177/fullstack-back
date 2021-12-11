from persistencia import guardar_pedido

with open("pedidos.txt", "w", encoding="utf-8") as file:
    file.write("")
    file.close()

# Esto es una lista de diccionarios, hay tres elementos: Pedro, Michael y Victor con sus correspondientes apellidos
pedidos = [{"nombre": "Pedro", "apellidos": "Gil de Diego"},
{"nombre": "Michael", "apellidos": "Jordan"},
{"nombre": "Victor", "apellidos": "Hernández"}]

### Idea: ¿Por qué no colectas cada diccionario de la lista y después imprimes lo que quieres de ese diccionario
# # Entonces recorre primero la lista: "pedidos":
for i in pedidos:
    # Ahora cada "item de la lista es un diccionario, usalo como diccionario e imprime lo que quieres de él.
    # Primero imprime el diccionario del item de la lista... solo por verlo
    print(i)
    #Ahora invoca el metodo 'guardar_pedido' de persistencia y que imprima en un archivo lo que le mandas (nombre y apellidos)
    guardar_pedido(i["nombre"],i["apellidos"])

#Manda un mensaje que has finalizado
print("Listo, ya escribí las 'key' solicitadas de cada diccionario de la lista 'pedidos' en el archivo Pedidos.txt")

