import numpy as np 

def function(x):

	h0 = 8
	a7 = 5
	x = x
	paths = []
	try:
		if x >= 8:
			x = x/3
			a7 = x/a7
			h0 = 6/h0
			paths.append(1)
		else:
			a7 = 3/a7
			x = 3*3
			paths.append(2)
		if h0 > 9:
			a7 = 3+a7
			paths.append(3)
		else:
			x = 9-x
			h0 = 5+5
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