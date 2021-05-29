import numpy as np 

def function(x):

	v2 = x
	v4 = x
	paths = []
	try:
		if v2 > 9:
			v2 = v2*3
			x = v2*8
			paths.append(1)
		else:
			v2 = v4/4
			v4 = 1-v4
			v2 = x/v2
			paths.append(2)
		if v2 > 8:
			v2 = 9+v2
			x = x-v4
			paths.append(3)
		else:
			v4 = 8/v4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v2 = x**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))