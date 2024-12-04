# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    D04-02_AoC.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdacal-a <jdacal-a@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/04 10:40:29 by jdacal-a          #+#    #+#              #
#    Updated: 2024/12/04 10:56:29 by jdacal-a         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests

# URL de la página con los datos
url = "https://adventofcode.com/2024/day/4/input"

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
else:
	raise Exception(f"Error al descargar los datos: {response.status_code}")

# Paso 2: Convertir el texto en un tablero bidimensional
board = [list(line) for line in lines]

# Paso 3: Función para contar patrones X-MAS
def count_x_mas_patterns(board):
	"""
	Cuenta la cantidad de patrones 'X-MAS' en el tablero.

	Args:
		board (list of list of str): El tablero como una lista de listas de caracteres.

	Returns:
		int: Número de patrones 'X-MAS' encontrados.
	"""
	# Dimensiones del tablero
	rows, cols = len(board), len(board[0])
	pattern_count = 0

	# Función auxiliar para validar un patrón MAS
	def is_mas(seq):
		return seq == "MAS" or seq == "SAM"

	# Explorar cada celda como el centro de la "X"
	for r in range(1, rows - 1):  # Evitar bordes
		for c in range(1, cols - 1):  # Evitar bordes
			# Obtener las diagonales
			top_left = board[r - 1][c - 1]
			top_right = board[r - 1][c + 1]
			center = board[r][c]
			bottom_left = board[r + 1][c - 1]
			bottom_right = board[r + 1][c + 1]

			# Construir los dos posibles "MAS"
			mas_1 = top_left + center + bottom_right
			mas_2 = top_right + center + bottom_left

			# Comprobar si ambos son válidos
			if is_mas(mas_1) and is_mas(mas_2):
				pattern_count += 1

	return pattern_count

# Paso 3: Ejecutar la función en el tablero importado
result = count_x_mas_patterns(board)

# Paso 4: Imprimir el resultado
print(f"Número de patrones 'X-MAS' encontrados: {result}")
