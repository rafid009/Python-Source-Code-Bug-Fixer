import numpy as np 

def function(x):

	y9 = 1
	q4 = 1
	paths = []
	try:
		if x < 8:
			q4 = 1-1
			q4 = 6*q4
			y9 = 9+q4
			paths.append(1)
		else:
			y9 = 6+y9
			q4 = q4*8
			y9 = y9*1
			paths.append(2)
		if y9 >= 7:
			y9 = y9-8
			x = x-y9
			q4 = y9*9
			paths.append(3)
		else:
			x = 5*x
			y9 = y9*6
			x = y9-x
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		y9 = y9**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))