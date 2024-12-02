# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    D02-02_AoC.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/02 21:06:09 by marvin            #+#    #+#              #
#    Updated: 2024/12/02 21:06:09 by marvin           ###   ########.fr        #
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

# Nueva función que incluye el Amortiguador de Problemas
def is_safe_with_dampener(report):
	# Si el informe ya es seguro, no necesitamos modificarlo
	if is_safe_report(report):
		return True

	# Convertimos los niveles a enteros
	levels = list(map(int, report.split()))

	# Intentamos eliminar cada nivel, uno por uno
	for i in range(len(levels)):
		# Creamos un nuevo informe sin el nivel i
		modified_levels = levels[:i] + levels[i+1:]

		# Convertimos la lista modificada de vuelta a un string
		modified_report = " ".join(map(str, modified_levels))

		# Si el informe modificado es seguro, este también lo es
		if is_safe_report(modified_report):
			return True

	# Si ninguna modificación funciona, el informe no es seguro
	return False

# Contador de informes seguros con el Amortiguador de Problemas
safe_reports_with_dampener = sum(1 for report in lines if is_safe_with_dampener(report))

# Mostrar el resultado
print(f"Total de informes seguros con el Amortiguador de Problemas: {safe_reports_with_dampener}")
