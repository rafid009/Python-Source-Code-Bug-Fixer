import numpy as np 

def function(x):

	n2 = 7
	y9 = 5
	paths = []
	try:
		if y9 <= 5:
			x = x*7
			n2 = 4+n2
			x = x/7
			paths.append(1)
		else:
			x = 7*2
			n2 = 7/n2
			n2 = 9*n2
			paths.append(2)
		if n2 < 3:
			y9 = y9/4
			y9 = 0-3
			paths.append(3)
		else:
			x = y9-n2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))