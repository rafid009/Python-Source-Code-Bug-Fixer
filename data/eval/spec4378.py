import numpy as np 

def function(x):

	y9 = x
	e4 = 2
	paths = []
	try:
		if x > 0:
			x = x-9
			x = 0*x
			e4 = e4-5
			paths.append(1)
		else:
			y9 = x*4
			e4 = 7+3
			paths.append(2)
		if x <= 0:
			e4 = e4-2
			y9 = 7*y9
			x = x/5
			paths.append(3)
		else:
			x = x/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e4 = x**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))