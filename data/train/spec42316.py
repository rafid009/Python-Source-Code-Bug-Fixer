import numpy as np 

def function(x):

	h3 = x
	w6 = 1
	paths = []
	try:
		if x <= 0:
			w6 = 8/5
			paths.append(1)
		else:
			h3 = h3*7
			paths.append(2)
		if x <= 0:
			h3 = x*4
			h3 = 6+6
			paths.append(3)
		else:
			x = h3+3
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