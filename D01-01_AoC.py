# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    D01-01_AoC.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/02 20:55:22 by marvin            #+#    #+#              #
#    Updated: 2024/12/02 20:55:22 by marvin           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests

# URL de la página con los datos
url = "https://adventofcode.com/2024/day/1/input"

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

	# Inicializar listas
	left_list = []
	right_list = []

	try:
		# Procesar cada línea para extraer los primeros y últimos 5 dígitos
		for line in lines:
			if len(line) < 10:
				raise ValueError("Una de las líneas tiene menos de 10 caracteres.")

			left_part = int(line[:5])  # Primeros 5 dígitos
			right_part = int(line[-5:])  # Últimos 5 dígitos

			left_list.append(left_part)
			right_list.append(right_part)

		# Verifica que ambas listas tengan el mismo tamaño
		if len(left_list) != len(right_list):
			raise ValueError("Las listas izquierda y derecha no tienen el mismo tamaño.")

		# Ordenar ambas listas
		left_list.sort()
		right_list.sort()

		# Paso 3: Calcular las distancias absolutas y sumarlas
		total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))

		# Resultado
		print("La distancia total entre las listas es:", total_distance)

	except ValueError as ve:
		print(f"Error al procesar los datos: {ve}")
else:
	print(f"Error al descargar los datos: {response.status_code}")
