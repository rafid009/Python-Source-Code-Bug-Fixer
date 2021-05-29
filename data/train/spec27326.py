import numpy as np 

def function(x):

	r6 = x
	y9 = x
	paths = []
	try:
		if x < 8:
			y9 = 6*1
			y9 = y9*x
			paths.append(1)
		else:
			r6 = 1*r6
			y9 = r6/r6
			paths.append(2)
		if x > 6:
			r6 = y9*9
			paths.append(3)
		else:
			r6 = x*y9
			r6 = 7-x
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