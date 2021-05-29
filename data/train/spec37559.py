import numpy as np 

def function(x):

	v8 = 9
	y9 = 3
	paths = []
	try:
		if y9 > 7:
			y9 = y9+0
			paths.append(1)
		else:
			v8 = v8/8
			x = x-8
			x = 7-x
			paths.append(2)
		if v8 <= 8:
			x = 1/x
			v8 = v8+5
			y9 = y9+7
			paths.append(3)
		else:
			v8 = v8*3
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