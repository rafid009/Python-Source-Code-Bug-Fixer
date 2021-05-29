import numpy as np 

def function(x):

	v9 = 9
	h2 = 9
	paths = []
	try:
		if x < 0:
			v9 = v9/6
			v9 = 8*v9
			paths.append(1)
		else:
			h2 = 3*h2
			paths.append(2)
		if x < 4:
			v9 = v9-v9
			h2 = x*v9
			paths.append(3)
		else:
			v9 = v9+5
			x = x*7
			x = v9*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h2 = x**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))