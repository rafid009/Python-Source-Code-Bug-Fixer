import numpy as np 

def function(x):

	r8 = 7
	y9 = 7
	paths = []
	try:
		if y9 < 8:
			x = 6-x
			r8 = x+4
			r8 = 9*r8
			paths.append(1)
		else:
			r8 = 0-x
			paths.append(2)
		if y9 <= 6:
			y9 = x-x
			y9 = 2-r8
			paths.append(3)
		else:
			y9 = r8-x
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		x = y9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))