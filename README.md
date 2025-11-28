# 🎮 Proyecto Final - Colección de Videojuegos (Lucas Figal)

## 🛠️ Pasos de Configuración

Este proyecto utiliza el framework **Django** y una base de datos **SQLite** para gestionar datos de videojuegos, consolas y empresas, con las siguientes configuraciones:

1. **Clonar el repositorio.**

2. **Crear y activar el entorno virtual** (revisar el archivo `requirements.txt` si es necesario instalar dependencias).

3. **Realizar Migraciones:** Asegurarse de que la base de datos esté actualizada con los modelos.

4. **Crear Superusuario:** Para acceder al administrador y gestionar datos de usuarios.

5. **Ejecutar el servidor local:**

El proyecto debería estar disponible en `http://127.0.0.1:8000/`.

## 💻 Uso de la Aplicación y Funcionalidades

El proyecto implementa un sistema completo de **Autenticación** y **CRUD** (Crear, Leer, Actualizar, Eliminar) para los tres modelos principales.

### 🗺️ Puntos de Acceso y Funcionalidades

| Ruta URL | Nombre de la Vista | Funcionalidad Clave |
| :--- | :--- | :--- |
| **`/`** | `views.inicio` | ✅ Índice principal y enlaces de navegación. |
| **`/usuarios/registro/`** | `RegistroUsuarioView` | ✅ Creación de nuevos usuarios (Autenticación). |
| **`/juegos/lista/**` | `views.lista_juegos` | ✅ Listado, Búsqueda y Mensaje de Aviso. |
| **`/juegos/agregar/**` | `views.crear_juego` | ✅ Creación de registros (Formulario ModelForm). |
| **`/juegos/detalle/<pk>/`** | `JuegoDetalle` | ✅ Detalle y acceso a edición/eliminación. |
| **`/acerca-de-mi/**` | `views.acerca_de_mi` | ✅ Contenido estático del autor/proyecto. |

### 📋 Pasos de Prueba (Orden de Prueba Recomendado para la Demostración)

1. **Autenticación:**
    * Registrar un nuevo usuario en `/usuarios/registro/`.
    * Iniciar sesión y cerrar sesión.

2. **CRUD Completo:**
    * Acceder a `/juegos/agregar/` y crear un nuevo juego, incluyendo una imagen (MEDIA).
    * Verificar que el listado se actualice.
    * Acceder al detalle del juego, luego **Editar** y **Eliminar** el registro.

3. **Búsqueda y Filtro:**
    * Utilizar la función de búsqueda para filtrar la lista de juegos por título.
    * Verificar que se muestre el "mensaje de aviso" si no hay resultados.

4. **Verificación Final:**
    * Acceder al Administrador de Django (`http://127.0.0.1:8000/admin/`) para verificar que los modelos de `Juego`, `Consola` y `Empresa` están registrados y que el modelo `User` está funcional.