import numpy as np 

def function(x):

	v4 = 7
	v1 = x
	paths = []
	try:
		if x <= 8:
			v4 = v4+v4
			paths.append(1)
		else:
			v4 = v4*8
			x = x*6
			paths.append(2)
		if x <= 2:
			x = 5/v1
			paths.append(3)
		else:
			x = 9+2
			v1 = 4+v1
			v1 = 5/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v4 = x**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))