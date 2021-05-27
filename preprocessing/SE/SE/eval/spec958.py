import numpy as np 

def function(x):

	b1 = x
	y9 = x
	paths = []
	try:
		if x > 0:
			y9 = y9+8
			paths.append(1)
		else:
			x = x/b1
			paths.append(2)
		if x > 5:
			b1 = b1+7
			x = x+x
			paths.append(3)
		else:
			x = 9*b1
			b1 = x/b1
			x = x/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b1 = x**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))