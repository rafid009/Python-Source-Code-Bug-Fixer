import numpy as np 

def function(x):

	y9 = 6
	w2 = 7
	paths = []
	try:
		if x > 9:
			x = w2-6
			y9 = 8/1
			paths.append(1)
		else:
			y9 = y9/w2
			w2 = w2+w2
			x = 0+x
			paths.append(2)
		if x <= 0:
			y9 = y9+w2
			y9 = y9*y9
			w2 = y9+3
			paths.append(3)
		else:
			y9 = y9/y9
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