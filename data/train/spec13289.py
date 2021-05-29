import numpy as np 

def function(x):

	y9 = 2
	l0 = 4
	paths = []
	try:
		if y9 < 9:
			y9 = y9+x
			paths.append(1)
		else:
			l0 = 0/l0
			paths.append(2)
		if y9 < 2:
			x = x+3
			paths.append(3)
		else:
			l0 = 7-l0
			y9 = y9-7
			l0 = 1-l0
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		y9 = l0**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))