import numpy as np 

def function(x):

	b5 = 8
	y9 = x
	paths = []
	try:
		if b5 > 2:
			b5 = x+0
			b5 = x-5
			b5 = b5-9
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if x < 7:
			y9 = 5+y9
			paths.append(3)
		else:
			y9 = 0*y9
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