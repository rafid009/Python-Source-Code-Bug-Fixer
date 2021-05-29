import numpy as np 

def function(x):

	y9 = x
	l4 = 2
	x = x
	paths = []
	try:
		if l4 > 1:
			x = l4/x
			y9 = 4-y9
			paths.append(1)
		else:
			l4 = 1/l4
			y9 = 4-y9
			paths.append(2)
		if x >= 3:
			l4 = y9/l4
			l4 = y9-l4
			paths.append(3)
		else:
			l4 = l4+9
			y9 = y9+l4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l4 = x**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))