import numpy as np 

def function(x):

	y9 = x
	a4 = x
	paths = []
	try:
		if x > 9:
			a4 = 7*0
			paths.append(1)
		else:
			x = 1+3
			paths.append(2)
		if a4 < 7:
			x = 8+a4
			paths.append(3)
		else:
			a4 = a4*a4
			a4 = y9*a4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y9 = x**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))