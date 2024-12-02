# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    D02-01_AoC.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/02 20:55:35 by marvin            #+#    #+#              #
#    Updated: 2024/12/02 20:55:35 by marvin           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests

# URL de la página con los datos
url = "https://adventofcode.com/2024/day/2/input"

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

# Función para verificar si una lista de niveles es segura
def is_safe_report(report):
	# Convertimos los niveles a enteros
	levels = list(map(int, report.split()))

	# Verificamos diferencias entre niveles consecutivos
	differences = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

	# Condición 1: Diferencias deben estar entre -3 y -1 (decreciente) o entre 1 y 3 (creciente)
	all_increasing = all(1 <= diff <= 3 for diff in differences)
	all_decreasing = all(-3 <= diff <= -1 for diff in differences)

	# Un informe es seguro si todas las diferencias son consistentes y cumplen las reglas
	return all_increasing or all_decreasing

# Contador de informes seguros
safe_reports_count = sum(1 for report in lines if is_safe_report(report))

# Mostrar el resultado
print(f"Total de informes seguros: {safe_reports_count}")
