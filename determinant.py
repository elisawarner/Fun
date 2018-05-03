# find determinant of nxn matrix
import numpy as np


test_matrix = np.matrix('1 2 3 4; 1 0 2 0; 0 1 2 3; 2 3 0 0 ')

DEBUG = False

def check_2x2_determinant(matrix):
	if matrix.shape == (2,2):
		return (matrix.item((0,0)) * matrix.item((1,1)))-(matrix.item((0,1)) * matrix.item((1,0)))
	return None

def check_nxn(matrix):
	if matrix.shape[0] == matrix.shape[1]:
		return True
	return False

def submatrix(matrix, index):
	# remove column
	matrix = np.delete(matrix, index, axis = 1)
	# remove row
	return matrix[1:,:]

def nxn_determinant(matrix, sum = 0):
	if DEBUG:
		print(matrix)
	if not check_nxn(matrix):
		print("Sorry, your matrix does not qualify for a determinant: ", matrix.shape)
		return None

	base_determinant = check_2x2_determinant(matrix)
	if type(base_determinant) == type(3):
		#print(base_determinant)
		return base_determinant

	if type(base_determinant) != type(3):
		for index in range(matrix[0,:].shape[1]):
			factor = matrix.item((0,index)) * (-1)**(index+1)

			sum += factor * (nxn_determinant(submatrix(matrix, index)))
			if DEBUG:
				print("SUM: %d" % sum)

		return sum

print("DETERMINANT:", nxn_determinant(test_matrix))
