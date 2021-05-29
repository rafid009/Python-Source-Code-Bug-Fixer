import numpy as np 

def function(x):

	h8 = x
	v3 = 2
	paths = []
	try:
		if v3 <= 9:
			v3 = 6+8
			h8 = h8-1
			paths.append(1)
		else:
			h8 = 2*7
			paths.append(2)
		if h8 < 6:
			x = 1+x
			h8 = h8+v3
			paths.append(3)
		else:
			h8 = 1-h8
			h8 = 1-x
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