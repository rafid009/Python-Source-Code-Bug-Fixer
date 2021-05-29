import numpy as np 

def function(x):

	e9 = x
	n0 = x
	paths = []
	try:
		if e9 > 5:
			x = 5+x
			paths.append(1)
		else:
			x = 3-x
			x = e9+8
			n0 = n0-n0
			paths.append(2)
		if n0 < 5:
			e9 = e9/9
			n0 = n0+8
			paths.append(3)
		else:
			x = x-x
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