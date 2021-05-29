import numpy as np 

def function(x):

	y9 = x
	e5 = x
	paths = []
	try:
		if e5 < 5:
			y9 = 4/y9
			y9 = x*y9
			paths.append(1)
		else:
			x = 8-x
			e5 = 5/5
			paths.append(2)
		if x > 1:
			y9 = 8+y9
			x = x+7
			x = e5-4
			paths.append(3)
		else:
			x = 7*x
			e5 = y9*5
			y9 = y9/y9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e5 = x**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))