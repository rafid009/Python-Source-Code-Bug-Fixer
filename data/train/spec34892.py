import numpy as np 

def function(x):

	v3 = 7
	h4 = 0
	paths = []
	try:
		if x < 8:
			v3 = h4+v3
			h4 = 7*v3
			paths.append(1)
		else:
			h4 = 5-h4
			paths.append(2)
		if v3 > 0:
			h4 = h4*9
			x = x-6
			h4 = h4*v3
			paths.append(3)
		else:
			h4 = 5+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h4 = x**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))