# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    D01-02_AoC.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/02 20:55:11 by marvin            #+#    #+#              #
#    Updated: 2024/12/02 20:55:11 by marvin           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests

# URL de la página con los datos
url = "https://adventofcode.com/2024/day/1/input"

# Token de sesión (si el contenido requiere autenticación)
session_token = "53616c7465645f5fe0f3bb6fbe23026a656434014c369f38d609c2007049bdb8f41080ebd263497dba705ff4f763e597884272873c98ba208d66fb73fa149a85"

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

		# Parte 2: Calcular la similaridad entre las listas
		similarity_score = 0
		for num in left_list:
			# Contar cuántas veces 'num' aparece en right_list
			count_in_right = right_list.count(num)
			# Incrementar el puntaje de similaridad
			similarity_score += num * count_in_right

		# Resultado
		print("El puntaje de similaridad es:", similarity_score)

	except ValueError as ve:
		print(f"Error al procesar los datos: {ve}")
else:
	print(f"Error al descargar los datos: {response.status_code}")
