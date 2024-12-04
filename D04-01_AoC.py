# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    D04-01_AoC.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdacal-a <jdacal-a@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/04 10:40:29 by jdacal-a          #+#    #+#              #
#    Updated: 2024/12/04 10:50:51 by jdacal-a         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests

# URL de la página con los datos
url = "https://adventofcode.com/2024/day/4/input"

# Token de sesión (si el contenido requiere autenticación)
session_token = "53616c7465645f5f318989a610f16460d9d34879d0529014a3ff7f455afabc1605e27f4f3876e82fc91e1dee5fd642bb77748e3f67aab54c2d6c0f7f955830f2"

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

# Paso 3: Definir la función para contar coincidencias
def count_xmas_matches(board):
	"""
	Cuenta todas las coincidencias de las secuencias "XMAS" y "SMAX" en un tablero bidimensional.

	Parámetros:
		board (list of list of str): Tablero bidimensional representado como una lista de listas.

	Retorna:
		int: Número total de coincidencias encontradas.
	"""
	# Secuencias objetivo
	targets = ["XMAS"]
	target_length = len(targets[0])

	# Dimensiones del tablero
	rows, cols = len(board), len(board[0])

	# Direcciones de búsqueda: (dx, dy)
	directions = [
		(0, 1),   # Derecha
		(0, -1),  # Izquierda
		(1, 0),   # Abajo
		(-1, 0),  # Arriba
		(1, 1),   # Diagonal abajo derecha
		(1, -1),  # Diagonal abajo izquierda
		(-1, 1),  # Diagonal arriba derecha
		(-1, -1), # Diagonal arriba izquierda
	]

	def is_within_bounds(x, y):
		"""Verifica si las coordenadas (x, y) están dentro de los límites del tablero."""
		return 0 <= x < rows and 0 <= y < cols

	def match_in_direction(x, y, dx, dy):
		"""
		Verifica si hay una coincidencia con alguna de las secuencias objetivo
		empezando desde (x, y) en la dirección (dx, dy).
		"""
		sequence = []
		for step in range(target_length):
			nx, ny = x + dx * step, y + dy * step
			if not is_within_bounds(nx, ny):
				return False
			sequence.append(board[nx][ny])
		return "".join(sequence) in targets

	# Contar coincidencias
	match_count = 0
	for x in range(rows):
		for y in range(cols):
			for dx, dy in directions:
				if match_in_direction(x, y, dx, dy):
					match_count += 1

	return match_count

# Paso 4: Contar coincidencias en el tablero descargado
result = count_xmas_matches(board)
print(f"Número total de coincidencias encontradas: {result}")

