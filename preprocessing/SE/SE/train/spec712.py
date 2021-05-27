import numpy as np 

def function(x):

	y9 = x
	o4 = x
	x = 1
	paths = []
	try:
		if y9 >= 7:
			x = 7*o4
			o4 = o4/8
			y9 = o4+y9
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if y9 >= 8:
			o4 = 8*x
			y9 = 5-y9
			y9 = y9-y9
			paths.append(3)
		else:
			x = 5+y9
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		o4 = o4**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))