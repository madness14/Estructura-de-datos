import random as precio

tienda = {
    'leche': precio.randint(1, 50),
    'cereal': precio.randint(1, 50),
    'pasta de dientes': precio.randint(1, 50),
    'huevo': precio.randint(1, 50),
    'salchicha': precio.randint(1, 50),
    'yogurt': precio.randint(1, 50),
    'pasta': precio.randint(1, 50),
    'enlatados': precio.randint(1, 50)
}

print("Productos en la tienda y sus precios:")
for producto, precio in tienda.items():
    print(producto, "- precio: $", precio)

producto_mas_caro = max(tienda, key=tienda.get)
precio_mas_caro = tienda[producto_mas_caro]

print("Producto mas caro:", producto_mas_caro, "- Precio: $", precio_mas_caro)
