import os
import sys
import time
from pathlib import Path
from rembg import remove
from PIL import Image

# Paleta de colores para la terminal
CYAN = '\033[96m'
MAGENTA = '\033[95m'
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def limpiar_pantalla():
    os.system('clear' if os.name == 'posix' else 'cls')

def efecto_escritura(texto, color=GREEN, velocidad=0.015, salto=True):
    sys.stdout.write(color)
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidad)
    if salto:
        sys.stdout.write(RESET + '\n')
    else:
        sys.stdout.write(RESET)

def obtener_directorio_salida():
    # Detectar el directorio base del usuario
    home = str(Path.home())
    ruta_imagenes = os.path.join(home, "Imágenes")
    
    # Fallback por si el sistema operativo usa "Pictures" en inglés
    if not os.path.exists(ruta_imagenes):
        ruta_imagenes = os.path.join(home, "Pictures")
        
    ruta_salida = os.path.join(ruta_imagenes, "PNGBOT")
    
    # Crear la carpeta PNGBOT si no existe
    if not os.path.exists(ruta_salida):
        os.makedirs(ruta_salida)
        
    return ruta_salida

def mostrar_banner():
    limpiar_pantalla()
    print(rf"""{CYAN}
  ╔════════════════════════════════════════════════════════╗
  ║ {MAGENTA}  ____  _   _  ____ ____   ___ _____                 {CYAN}║
  ║ {MAGENTA} |  _ \| \ | |/ ___| __ ) / _ \_   _|                {CYAN}║
  ║ {MAGENTA} | |_) |  \| | |  _|  _ \| | | || |                  {CYAN}║
  ║ {MAGENTA} |  __/| |\  | |_| | |_) | |_| || |                  {CYAN}║
  ║ {MAGENTA} |_|   |_| \_|\____|____/ \___/ |_|                  {CYAN}║
  ║                                                        ║
  ║ {YELLOW}> SISTEMA DE EXTRACCIÓN DE FONDOS INICIADO           {CYAN}║
  ║ {YELLOW}> MOTOR: rembg_neural_network                        {CYAN}║
  ╚════════════════════════════════════════════════════════╝{RESET}
    """)

def procesar_imagen(ruta_entrada, nombre_salida):
    directorio_destino = obtener_directorio_salida()
    ruta_completa_salida = os.path.join(directorio_destino, nombre_salida)
    
    try:
        efecto_escritura(f"[*] Leyendo imagen: {ruta_entrada}...", YELLOW)
        input_image = Image.open(ruta_entrada)
        
        efecto_escritura("[*] Procesando recorte con IA...", MAGENTA)
        output_image = remove(input_image)
        
        output_image.save(ruta_completa_salida, "PNG")
        efecto_escritura(f"[+] EXTRACCIÓN EXITOSA -> {ruta_completa_salida}\n", GREEN)
    except Exception as e:
        efecto_escritura(f"[-] ERROR DEL SISTEMA: {e}\n", RED)

def main():
    while True:
        mostrar_banner()
        print(f"{CYAN}[1]{RESET} Procesar archivo individual")
        print(f"{CYAN}[2]{RESET} Procesar directorio completo (Lote)")
        print(f"{RED}[3]{RESET} Salir")
        
        opcion = input(f"\n{GREEN}pngbot> {RESET}")

        if opcion == '1':
            ruta = input(f"{YELLOW}Ruta de la imagen (ej: foto.jpg): {RESET}")
            if os.path.exists(ruta):
                nombre_base = os.path.basename(ruta)
                nombre_sin_ext, _ = os.path.splitext(nombre_base)
                nombre_salida = f"{nombre_sin_ext}_nobg.png"
                procesar_imagen(ruta, nombre_salida)
                input(f"{CYAN}Presiona Enter para continuar...{RESET}")
            else:
                efecto_escritura("[-] Archivo no encontrado.", RED)
                time.sleep(2)

        elif opcion == '2':
            directorio = input(f"{YELLOW}Ruta del directorio de imágenes: {RESET}")
            if os.path.exists(directorio) and os.path.isdir(directorio):
                archivos = [f for f in os.listdir(directorio) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
                
                if not archivos:
                    efecto_escritura("[-] No se detectaron archivos de imagen válidos.", RED)
                else:
                    efecto_escritura(f"[+] Se detectaron {len(archivos)} imágenes. Iniciando procesamiento...\n", MAGENTA)
                    for archivo in archivos:
                        ruta_completa = os.path.join(directorio, archivo)
                        nombre_sin_ext, _ = os.path.splitext(archivo)
                        nombre_salida = f"{nombre_sin_ext}_nobg.png"
                        
                        if not archivo.endswith('_nobg.png'):
                            procesar_imagen(ruta_completa, nombre_salida)
                input(f"{CYAN}Presiona Enter para continuar...{RESET}")
            else:
                efecto_escritura("[-] Directorio inválido o inaccesible.", RED)
                time.sleep(2)

        elif opcion == '3':
            efecto_escritura("\n[!] Cerrando PNGBOT...", RED)
            time.sleep(1)
            limpiar_pantalla()
            sys.exit(0)
            
        else:
            efecto_escritura("[-] Comando no reconocido.", RED)
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        efecto_escritura("\n\n[!] Interrupción forzada detectada. Saliendo...", RED)
        sys.exit(0)