import numpy as np 

def function(x):

	h3 = 1
	v1 = 8
	paths = []
	try:
		if h3 < 8:
			v1 = x+x
			v1 = v1/5
			v1 = 3-3
			paths.append(1)
		else:
			x = h3*7
			v1 = h3+x
			paths.append(2)
		if h3 > 5:
			x = x*9
			x = 5-x
			paths.append(3)
		else:
			v1 = 8+6
			h3 = h3-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h3 = x**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))