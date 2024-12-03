# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    D03-01_AoC.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/03 21:12:13 by marvin            #+#    #+#              #
#    Updated: 2024/12/03 21:12:13 by marvin           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests
import re

# URL de la página con los datos
url = "https://adventofcode.com/2024/day/3/input"

# Token de sesión (si el contenido requiere autenticación)
session_token = "SESSION TOKEN"

# Cabecera con la cookie de autenticación
headers = {
	"Cookie": f"session={session_token}"
}

# Paso 1: Descargar los datos desde la web
response = requests.get(url, headers=headers)
if response.status_code == 200:
	# Leer y procesar las listas desde el contenido descargado
	input_data = response.text.strip()  # Elimina espacios en blanco iniciales y finales
	lines = input_data.splitlines()  # Divide por líneas

def sumar_mul_operaciones_desde_lineas(lines):
	"""
	Procesa una lista de líneas para extraer y calcular la suma de todas las operaciones mul(x, y).

	:param lines: list[str] - Lista de líneas de texto
	:return: int o float - La suma de todas las operaciones mul(x, y) encontradas
	"""
	total_suma = 0

	# Procesamos cada línea
	for line in lines:
		# Buscamos todas las operaciones mul(x, y) en la línea
		operaciones = re.findall(r"mul\((\d+),\s*(\d+)\)", line)

		# Calculamos el producto para cada operación encontrada y actualizamos la suma total
		total_suma += sum(int(x) * int(y) for x, y in operaciones)

	return total_suma

# Uso con las líneas descargadas
resultado = sumar_mul_operaciones_desde_lineas(lines)
print(f"La suma total de todas las operaciones mul es: {resultado}")
