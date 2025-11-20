# 🚀 Pre-Entrega N°3 - Lucas Figal

## 🛠️ Pasos de Configuración

Este proyecto utiliza el framework Django y una base de datos SQLite para gestionar datos de videojuegos, consolas y empresas de videojuegos.

1.  **Clonar el repositorio.**

2.  **Crear y activar el entorno virtual** (revisar el archivo `requirements.txt` si es necesario instalar dependencias).

3.  **Realizar Migraciones:** Asegurarse de que la base de datos esté actualizada con los modelos

4.  **(Opcional) Crear Superusuario:** Para verificar los datos a través del Administrador de Django

5.  **Ejecutar el servidor local:**

    El proyecto debería estar disponible en `http://127.0.0.1:8000/`.

---

## 💻 Uso de la Aplicación y Funcionalidades

El proyecto implementa la inserción de datos a través de **tres formularios ModelForm** (uno por cada modelo) y una función de **búsqueda** que utiliza parámetros GET.

### 🗺️ Puntos de Acceso y Funcionalidades

| Ruta URL | Nombre de la Vista | Requisito Cumplido |
| :--- | :--- | :--- |
| **`/`** | `views.inicio` |✅ Índice completo de navegación. |
| **`/agregar-juego/`** | `views.crear_juego` | ✅ Formulario de Inserción (Modelo Juego). |
| **`/agregar-consola/`** | `views.crear_consola` | ✅ Formulario de Inserción (Modelo Consola). |
| **`/agregar-empresa/`** | `views.crear_empresa` | ✅ Formulario de Inserción (Modelo Empresa). |
| **`/buscar/`** | `views.buscar_juego` | ✅ Formulario/Lógica de Búsqueda. |
| **`/lista/`** | `views.lista_juegos` |✅ Listado de datos guardados. |

### Pasos de Prueba (Orden de Prueba Recomendado)

1.  **Inserción:** Acceder a las rutas `/agregar-juego/`, `/agregar-consola/`, y `/agregar-empresa/`. Llenar y enviar los formularios.
2.  **Verificación Post-Inserción:** Después de guardar, la aplicación **redirige automáticamente** al listado correspondiente (e.g., al guardar un juego, redirige a `/lista/`).
3.  **Búsqueda:** Acceder a la ruta `/buscar/` y probar la búsqueda por nombre parcial o completo de los Juegos que se acaban de guardar.
4.  **Verificación Avanzada:** Acceder al Administrador de Django (`http://127.0.0.1:8000/admin/`) para verificar la integridad de los datos en los tres modelos creados.