## README_TEST_FRONT_2 - Pruebas completas (Frontend + Backend + BD)

### 1. Objetivo
Este manual contiene **mas casos de prueba** para validar el frontend completo,
incluyendo flujos, permisos, validaciones y verificacion en base de datos.

### 2. Requisitos previos
- PostgreSQL instalado y corriendo
- Backend y frontend levantados
- Usuario admin existente

### 3. Casos de prueba adicionales

#### 3.1 Crear multiples usuarios y validar roles en BD
- Crear 2 docentes y 2 estudiantes desde el frontend.
- Validar en BD:
```
SELECT email FROM users
WHERE email IN ('docente2@ud.edu','docente3@ud.edu','est2@ud.edu','est3@ud.edu');
```

#### 3.2 Cambiar nombre de usuario y verificar
- Actualizar nombre de un docente.
- Validar en BD:
```
SELECT full_name FROM users WHERE email = 'docente2@ud.edu';
```

#### 3.3 Desactivar usuario y probar login
- Desactivar docente y luego intentar login.
- Resultado esperado: acceso denegado.
- Validar en BD:
```
SELECT is_active FROM users WHERE email = 'docente2@ud.edu';
```

#### 3.4 Materia con mismo codigo
- Crear materia con code duplicado.
- Resultado esperado: error 409.
- Validar en BD:
```
SELECT COUNT(*) FROM subjects WHERE code = 'MAT101';
```

#### 3.5 Periodo con fecha invalida
- Crear periodo con end_date menor a start_date.
- Resultado esperado: error 422.
- Validar en BD:
```
SELECT COUNT(*) FROM periods WHERE code = '2026-0';
```

#### 3.6 Inscripcion duplicada
- Crear la misma inscripcion (mismo estudiante, materia, periodo).
- Resultado esperado: error 409.
- Validar en BD:
```
SELECT COUNT(*) FROM enrollments
WHERE user_id = <ID_ESTUDIANTE>
  AND subject_id = <ID_MATERIA>
  AND period_id = <ID_PERIODO>;
```

#### 3.7 Inscripcion con materia inactiva
- Desactivar materia y crear inscripcion nueva.
- Resultado esperado: error por materia inactiva.
- Validar en BD:
```
SELECT is_active FROM subjects WHERE id = <ID_MATERIA>;
```

#### 3.8 Inscripcion con periodo inactivo
- Desactivar periodo y crear inscripcion nueva.
- Resultado esperado: error por periodo inactivo.
- Validar en BD:
```
SELECT is_active FROM periods WHERE id = <ID_PERIODO>;
```

#### 3.9 Calificacion con inscripcion inactiva
- Cancelar inscripcion y registrar calificacion.
- Resultado esperado: error por inscripcion inactiva.
- Validar en BD:
```
SELECT * FROM grades WHERE enrollment_id = <ID_INSCRIPCION>;
```

#### 3.10 Limites de calificacion
- Registrar nota 0 y 100.
- Resultado esperado: se guardan.
- Validar en BD:
```
SELECT value FROM grades
WHERE enrollment_id = <ID_INSCRIPCION>
ORDER BY id DESC LIMIT 2;
```

#### 3.11 Prueba de rol estudiante
- Estudiante intenta entrar a `/admin`.
- Resultado esperado: denied.

#### 3.12 Prueba de rol docente
- Docente intenta entrar a `/admin/users`.
- Resultado esperado: denied.

#### 3.13 Sesion en memoria
- Login admin, refrescar pagina.
- Resultado esperado: vuelve a login.

#### 3.14 Validaciones visuales
- Enviar formularios vacios.
- Resultado esperado: mensajes requeridos.

#### 3.15 Integridad de datos
- Verificar relaciones:
```
SELECT e.id, u.email, s.name, p.name
FROM enrollments e
JOIN users u ON u.id = e.user_id
JOIN subjects s ON s.id = e.subject_id
JOIN periods p ON p.id = e.period_id;
```
