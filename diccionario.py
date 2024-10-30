usuario ={"nombre": "Juan", "apellido": "Hernandez", "edad": 32}
print(usuario["nombre"])
usuario["profesion"] = "desarrollador de software"
print(usuario)

del usuario["edad"]

listaClaves= usuario.keys()
print(listaClaves)

valores = usuario.values()
print(valores)
usuario.update({"ciudad": "Madrid"})
print(usuario)