import numpy as np 

def function(x):

	v8 = 0
	y9 = x
	x = 7
	paths = []
	try:
		if y9 > 2:
			x = v8+x
			paths.append(1)
		else:
			v8 = 7-0
			paths.append(2)
		if v8 <= 8:
			x = x+y9
			v8 = 6*y9
			x = 2*7
			paths.append(3)
		else:
			x = 0-3
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		v8 = y9**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))