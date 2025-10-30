#!/bin/bash
# Crear carpeta de destino si no existe
mkdir -p backup

# Definir las rutas
origen="/home/esthersf/basic-scripting/files"
destino="/home/esthersf/AyscomAcademy/scriptlesson/backup" 

# Copiar todos los archivos .csv
cp "$origen"/*.csv "$destino/"

# Mensaje de confirmación
echo "✅ Archivos .csv copiados desde $origen a $destino"
