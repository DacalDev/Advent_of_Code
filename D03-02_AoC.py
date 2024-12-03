# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    D03-02_AoC.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/03 21:29:59 by marvin            #+#    #+#              #
#    Updated: 2024/12/03 21:29:59 by marvin           ###   ########.fr        #
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

# Función para procesar las instrucciones
def sum_enabled_multiplications(lines):
	# Patrón para encontrar instrucciones
	mul_pattern = r"mul\((\d+),(\d+)\)"  # Captura mul(x, y)
	do_pattern = r"do\(\)"               # Habilitar mul
	dont_pattern = r"don't\(\)"          # Deshabilitar mul

	enabled = True  # Estado inicial: mul habilitado
	total_sum = 0   # Suma total de las multiplicaciones habilitadas

	for line in lines:
		# Procesar cada línea en orden
		for match in re.finditer(f"{mul_pattern}|{do_pattern}|{dont_pattern}", line):
			if match.group(0).startswith("mul"):
				# Extraer los valores x, y y calcular el producto si está habilitado
				if enabled:
					x, y = int(match.group(1)), int(match.group(2))
					total_sum += x * y
			elif match.group(0) == "do()":
				# Habilitar mul
				enabled = True
			elif match.group(0) == "don't()":
				# Deshabilitar mul
				enabled = False

	return total_sum

# Usar la función con las líneas descargadas
result = sum_enabled_multiplications(lines)
print(result)  # Imprime el resultado de la suma de las multiplicaciones habilitadas
