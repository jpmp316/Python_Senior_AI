# Acceso y actualización de diccionarios

usuarios = {
    "u001": {"nombre": "Ana", "correo": "ana@mail.com", "roles": ["admin"]},
    "u002": {"nombre": "Pedro", "correo": "pedro@mail.com", "roles": ["cliente"]}
}

# Acceder alnombre del usuario "u001"
print("Nombre del u001: ", usuarios['u001']['nombre'])

# Agregar un nuevo rol al usuario"u002"
usuarios['u002']['roles'].append('ventas')
print("Roles actualizados del usuario u002: ", usuarios['u002']['roles'])

# Agregar un nuevo usuario
usuarios['u003'] = {"nombre": "Carlos", "correo": "carlos@mail.com", "roles": ["comprador"]}
usuarios['u004'] = {"nombre": "Jose", "correo": "jose@mail.com", "roles": ["secretario"]}

# Imprimir los usuarios registrados
print("\nListado de usuarios registrados:")
for id_usuario, valores_usuario in usuarios.items():
    print(f"{id_usuario} - {valores_usuario}")
    
# Buscar un usuario de acuerdo a su rol
rol = "comprador"
print(f"\nBuscar el rol {rol}")
for id_usuario, valores_usuario in usuarios.items():
    if rol in valores_usuario.get("roles", []):
        print(f"Usuario: {id_usuario} - Nombre: {valores_usuario['nombre']}")