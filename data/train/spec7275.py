import numpy as np 

def function(x):

	y9 = 9
	e2 = x
	paths = []
	try:
		if e2 > 9:
			x = x/6
			y9 = y9*8
			e2 = y9+2
			paths.append(1)
		else:
			y9 = 6-0
			paths.append(2)
		if y9 < 0:
			y9 = y9+4
			e2 = e2-x
			paths.append(3)
		else:
			e2 = y9/7
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e2 = x**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))