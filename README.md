# PNGBOT 🤖🖼️

PNGBOT es una herramienta de línea de comandos (CLI) que permite extraer el fondo de tus imágenes de forma automática utilizando inteligencia artificial (`rembg`). 

La aplicación gestiona su propio entorno virtual de Python para no interferir con las dependencias de tu sistema y guarda todos los resultados de forma ordenada en una carpeta dedicada dentro de tus Imágenes.

## ✨ Características

- **Interfaz CLI interactiva:** Menú sencillo y rápido de usar directamente en tu terminal.
- **Procesamiento individual:** Quita el fondo a una sola imagen.
- **Procesamiento por lotes:** Analiza un directorio completo y quita el fondo a todas las imágenes compatibles (`.png`, `.jpg`, `.jpeg`, `.webp`).
- **Gestión automática de dependencias:** Crea su propio `venv` e instala los módulos necesarios de forma transparente.
- **Comando global:** Ejecuta la herramienta desde cualquier directorio usando el comando `pngbot`.
- **Salida organizada:** Las imágenes procesadas se guardan automáticamente en `~/Imágenes/PNGBOT`.

## ⚙️ Requisitos previos

- Sistema operativo Linux o macOS.
- **Python 3** instalado en el sistema.
- Conexión a internet (solo para la primera ejecución, ya que descargará el modelo de IA y las dependencias).

## 🚀 Instalación y Configuración

Sigue estos pasos para clonar el repositorio y configurar el comando global en tu terminal:

**1. Clona este repositorio y entra a la carpeta:**
```bash
git clone [https://github.com/TU-USUARIO/pngbot.git](https://github.com/TU-USUARIO/pngbot.git)
cd pngbot