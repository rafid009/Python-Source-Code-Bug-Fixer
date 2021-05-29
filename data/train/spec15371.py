import numpy as np 

def function(x):

	y9 = x
	a5 = 4
	paths = []
	try:
		if x < 5:
			y9 = 6*y9
			y9 = 2/y9
			paths.append(1)
		else:
			a5 = 1-a5
			paths.append(2)
		if y9 <= 3:
			x = x-7
			paths.append(3)
		else:
			y9 = y9*y9
			x = x*2
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