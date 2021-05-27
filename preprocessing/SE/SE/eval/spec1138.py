import numpy as np 

def function(x):

	p8 = 9
	y9 = x
	paths = []
	try:
		if p8 <= 0:
			p8 = p8-p8
			paths.append(1)
		else:
			x = x*p8
			x = 9+x
			p8 = p8-1
			paths.append(2)
		if p8 >= 6:
			y9 = y9+y9
			y9 = 0-x
			paths.append(3)
		else:
			y9 = y9-p8
			p8 = p8*1
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