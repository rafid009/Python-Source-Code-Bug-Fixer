import numpy as np 

def function(x):

	a7 = x
	y9 = x
	paths = []
	try:
		if x > 0:
			a7 = a7*x
			paths.append(1)
		else:
			y9 = 4+y9
			paths.append(2)
		if a7 >= 9:
			y9 = 3-x
			paths.append(3)
		else:
			a7 = a7*2
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