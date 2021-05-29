import numpy as np 

def function(x):

	y9 = 4
	w6 = x
	paths = []
	try:
		if y9 >= 7:
			x = x-5
			x = x-x
			paths.append(1)
		else:
			y9 = y9*7
			x = x-5
			paths.append(2)
		if y9 <= 2:
			x = x+4
			w6 = w6+x
			paths.append(3)
		else:
			x = x*w6
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