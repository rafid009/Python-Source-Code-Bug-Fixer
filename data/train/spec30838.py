import numpy as np 

def function(x):

	n8 = 2
	y9 = 4
	paths = []
	try:
		if x <= 8:
			y9 = 7/y9
			n8 = 4-n8
			n8 = 6+n8
			paths.append(1)
		else:
			x = 2+x
			n8 = n8+8
			x = x*8
			paths.append(2)
		if x <= 2:
			n8 = y9/n8
			y9 = 6+y9
			paths.append(3)
		else:
			x = n8-x
			y9 = x*6
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