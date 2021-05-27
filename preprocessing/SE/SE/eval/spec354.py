import numpy as np 

def function(x):

	h0 = 3
	y3 = x
	paths = []
	try:
		if x > 0:
			x = 5*x
			paths.append(1)
		else:
			y3 = y3/4
			paths.append(2)
		if x > 4:
			x = 1+3
			paths.append(3)
		else:
			y3 = y3-y3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h0 = x**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))