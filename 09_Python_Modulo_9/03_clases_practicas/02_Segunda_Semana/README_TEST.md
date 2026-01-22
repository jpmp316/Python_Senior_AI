## README_TEST - Validación manual de APIs

### 1. Introducción

Este documento explica cómo **probar manualmente** los endpoints del backend Universidad Digital.
Una “API validada” significa que **responde correctamente**, **respeta roles/ownership**, y **retorna códigos HTTP esperados**.
Alcance: solo pruebas manuales (Swagger UI, Postman, cURL).

### 2. Herramientas recomendadas

- **Swagger UI (`/docs`)**: explorar endpoints, schemas y ejecutar requests rápidas.
- **Postman**: pruebas repetibles con entornos y colecciones.
- **cURL**: validaciones rápidas desde consola.

### 3. Preparación del entorno

Variables mínimas en `.env` (prefijo `APP_`):

```
APP_ENV=development
APP_DATABASE_URL=postgresql+psycopg://user:pass@localhost:5432/universidad
APP_JWT_SECRET=change_me
APP_CORS_ORIGINS=http://localhost:3000
```

Levantar backend:

```
uvicorn app.main:app --reload
```

URL base:

```
http://127.0.0.1:8000
```

### 4. Autenticación y autorización

#### 4.1 Login

- **Endpoint**: `POST /auth/login`
- **Payload**:
```
{
  "email": "admin@ud.edu",
  "password": "AdminPass1234"
}
```
- **Response 200**:
```
{
  "access_token": "jwt...",
  "token_type": "bearer"
}
```
- El token también se entrega como **cookie HttpOnly**.

#### 4.2 Uso del token

Header recomendado:

```
Authorization: Bearer <access_token>
```

Errores:
- **401**: token inválido o no enviado.
- **403**: token válido sin permisos.

### 5. Endpoints por dominio (formato estándar)

Formato por endpoint:
- URL
- Método HTTP
- Roles permitidos
- Headers requeridos
- Request body (JSON)
- Response exitosa
- Response de error
- Código HTTP esperado

#### Auth

**Login**
- URL: `/auth/login`
- Método: `POST`
- Roles: público
- Headers: `Content-Type: application/json`
- Body:
```
{"email":"admin@ud.edu","password":"AdminPass1234"}
```
- 200:
```
{"access_token":"jwt...","token_type":"bearer"}
```
- 401:
```
{"detail":"Credenciales inválidas."}
```

**Logout**
- URL: `/auth/logout`
- Método: `POST`
- Roles: autenticado
- Headers: `Authorization: Bearer <token>`
- Body: vacío
- 204 sin body
- 401 si no hay token

**Me**
- URL: `/auth/me`
- Método: `GET`
- Roles: autenticado
- Headers: `Authorization: Bearer <token>`
- 200:
```
{"id":1,"email":"admin@ud.edu","full_name":"Admin","is_active":true,"created_at":"...","roles":["Administrador"]}
```

#### Usuarios

**Crear usuario**
- URL: `/users`
- Método: `POST`
- Roles: Administrador
- Headers: `Authorization`
- Body:
```
{"email":"docente@ud.edu","full_name":"Docente Uno","password":"DocentePass1234","role_ids":[2]}
```
- 201:
```
{"id":2,"email":"docente@ud.edu","full_name":"Docente Uno","is_active":true,"created_at":"...","roles":["Docente"]}
```
- 409 si email duplicado

**Listar usuarios**
- URL: `/users`
- Método: `GET`
- Roles: Administrador
- Headers: `Authorization`
- 200: lista de usuarios

**Actualizar usuario**
- URL: `/users/{id}`
- Método: `PUT`
- Roles: Administrador
- Headers: `Authorization`
- Body:
```
{"full_name":"Docente Uno A","is_active":true}
```
- 200: usuario actualizado

**Cambiar estado (desactivar)**
- URL: `/users/{id}`
- Método: `DELETE`
- Roles: Administrador
- Headers: `Authorization`
- 200: usuario con `is_active=false`

#### Materias

**Crear materia**
- URL: `/subjects`
- Método: `POST`
- Roles: Administrador
- Headers: `Authorization`
- Body:
```
{"code":"MAT101","name":"Cálculo I","credits":4}
```
- 201: materia creada

**Listar materias**
- URL: `/subjects`
- Método: `GET`
- Roles: Administrador, Docente, Estudiante
- Headers: `Authorization`
- 200: lista de materias

**Actualizar materia**
- URL: `/subjects/{id}`
- Método: `PUT`
- Roles: Administrador
- Headers: `Authorization`
- Body:
```
{"name":"Cálculo I (actualizado)","credits":5}
```
- 200: materia actualizada

**Desactivar materia**
- URL: `/subjects/{id}`
- Método: `DELETE`
- Roles: Administrador
- Headers: `Authorization`
- 200: materia con `is_active=false`

#### Inscripciones

**Inscribir estudiante**
- URL: `/enrollments`
- Método: `POST`
- Roles: Administrador, Estudiante
- Headers: `Authorization`
- Body:
```
{"user_id":3,"subject_id":1,"period_id":1}
```
- 201: inscripción creada
- 409 si el estudiante intenta inscribir a otro usuario

**Consultar inscripciones**
- URL: `/enrollments`
- Método: `GET`
- Roles: Administrador, Docente, Estudiante
- Headers: `Authorization`
- 200: lista (estudiante solo ve las suyas)

**Cancelar inscripción**
- URL: `/enrollments/{id}`
- Método: `DELETE`
- Roles: Administrador
- Headers: `Authorization`
- 200: inscripción con `is_active=false`

#### Calificaciones

**Registrar calificación**
- URL: `/grades`
- Método: `POST`
- Roles: Administrador, Docente
- Headers: `Authorization`
- Body:
```
{"enrollment_id":1,"value":95.5,"notes":"Parcial 1"}
```
- 201: calificación creada

**Consultar calificaciones**
- URL: `/grades`
- Método: `GET`
- Roles: Administrador, Docente, Estudiante
- Headers: `Authorization`
- 200: lista (estudiante solo ve las suyas)

**Actualizar calificación**
- URL: `/grades/{id}`
- Método: `PUT`
- Roles: Administrador, Docente
- Headers: `Authorization`
- Body:
```
{"value":98.0,"notes":"Actualización"}
```
- 200: calificación actualizada

### 6. Validación de roles y permisos

**Acceso permitido (Administrador crea materia)**
```
POST /subjects
Authorization: Bearer <admin_token>
```
**200/201** esperado.

**Acceso denegado por rol (Estudiante crea materia)**
```
POST /subjects
Authorization: Bearer <student_token>
```
**403** esperado:
```
{"detail":"Permisos insuficientes."}
```

**Acceso denegado por ownership (Estudiante consulta inscripción ajena)**
```
GET /enrollments/999
Authorization: Bearer <student_token>
```
**409** esperado:
```
{"detail":"Acceso no permitido."}
```

### 7. Validación de errores comunes

- **400**: conflictos de negocio (ej. contraseña corta para docente/admin).
- **401**: no autenticado o token inválido.
- **403**: rol sin permisos.
- **404**: recurso inexistente.
- **422**: validación Pydantic (campos faltantes o tipos inválidos).

### 8. Uso de Swagger / OpenAPI

- Acceso: `http://127.0.0.1:8000/docs`
- Probar endpoints directamente con “Try it out”.
- Los schemas reflejan validaciones Pydantic.
- Respuestas y códigos están visibles por endpoint.

### 9. Checklist de validación

- [ ] Login funciona
- [ ] Token JWT válido en headers
- [ ] CRUD de usuarios probado
- [ ] CRUD de materias probado
- [ ] Inscripciones con ownership
- [ ] Calificaciones con ownership
- [ ] Roles respetados
- [ ] Respuestas claras y seguras
- [ ] No se exponen datos sensibles

### 10. Conclusión

Si todos los ítems del checklist se cumplen, las APIs están listas para consumo manual por frontend y validación funcional básica.
