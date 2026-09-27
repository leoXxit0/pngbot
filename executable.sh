#!/bin/bash

# Asegurar que el script opere en la carpeta donde está guardado
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

# Colores para los mensajes
CYAN='\033[0;96m'
GREEN='\033[0;92m'
YELLOW='\033[0;93m'
NC='\033[0m' # Sin color

echo -e "${CYAN}[*] Iniciando entorno de PNGBOT...${NC}"

# Verificar si existe la carpeta del entorno virtual (venv)
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}[!] Entorno virtual no detectado. Construyendo 'venv'...${NC}"
    python3 -m venv venv
fi

# Activar el entorno virtual
echo -e "${GREEN}[+] Activando entorno aislado...${NC}"
source venv/bin/activate

# Verificar si la dependencia (rembg) está instalada
if ! pip show rembg > /dev/null 2>&1; then
    echo -e "${YELLOW}[!] Dependencias no encontradas. Instalando rembg y pillow...${NC}"
    pip install "rembg[cpu]" pillow
else
    echo -e "${GREEN}[+] Dependencias operativas.${NC}"
fi

# Ejecutar la aplicación principal
echo -e "${GREEN}[+] Lanzando PNGBOT...${NC}"
sleep 1
python3 pngbot.py

# Salir limpiamente del entorno virtual al cerrar la app
deactivate