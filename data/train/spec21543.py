import numpy as np 

def function(x):

	y9 = x
	o8 = 1
	paths = []
	try:
		if y9 > 4:
			y9 = x*y9
			y9 = 3/y9
			paths.append(1)
		else:
			o8 = o8/4
			paths.append(2)
		if y9 >= 8:
			o8 = o8+o8
			paths.append(3)
		else:
			o8 = o8-x
			x = 6+x
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		x = y9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))