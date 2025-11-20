# 🚀 Pre-Entrega N°3 - Lucas Figal

## 🛠️ Pasos de Configuración

1.  **Clonar el repositorio.**
    
2.  **Crear y activar el entorno virtual.** (revisar el archivo `requirements.txt`).
    
3.  **Realizar Migraciones.**
    
4.  **(Opcional) Crear Superusuario.** 
    
5.  **Ejecutar el servidor local.**
    
    El proyecto debería estar disponible en `http://127.0.0.1:8000/`.

---

## 💻 Uso de la Aplicación (Sistema de Formularios Funcional)

Se trata de una aplicación Django que registra una lista de juegos (Nombre y Género) en una base de datos SQLite.

**La funcionalidad central de esta entrega es la lógica de subir datos mediante un Formulario (POST), no por parámetros de URL.**

### 🗺️ Rutas y Funcionalidades Principales

| Ruta URL | Nombre de la Vista | Funcionalidad |
| :--- | :--- | :--- |
| **`/`** | `views.inicio` | Página de bienvenida con enlaces de navegación. |
| **`/agregar/`** | `views.crear_juego` | **Formulario de Carga:** Permite introducir y subir un nuevo juego a la base de datos mediante un formulario web. |
| **`/lista/`** | `views.lista_juegos` | **Visualización:** Muestra todos los juegos listados hasta el momento en la base de datos. |

### Pasos de Prueba

1.  Acceder a la URL de carga: `http://127.0.0.1:8000/agregar/`.
2.  Introducir un **Nombre** y **Género** en el formulario.
3.  Al hacer clic en **"Guardar Juego"**, la aplicación guarda el dato y redirige automáticamente a la URL `/lista/`.
4.  Los datos también pueden ser verificados en el Administrador de Django (`http://127.0.0.1:8000/admin/`).

---