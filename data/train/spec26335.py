import numpy as np 

def function(x):

	r3 = 8
	y9 = 8
	paths = []
	try:
		if r3 <= 1:
			x = x/6
			y9 = 6*2
			x = 5*x
			paths.append(1)
		else:
			x = x*x
			y9 = y9*y9
			paths.append(2)
		if y9 <= 2:
			x = r3/5
			r3 = r3-3
			x = 0+x
			paths.append(3)
		else:
			x = 8/y9
			y9 = y9*r3
			x = x-4
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