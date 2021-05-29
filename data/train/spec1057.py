import numpy as np 

def function(x):

	h3 = 3
	x2 = x
	paths = []
	try:
		if x2 < 7:
			x2 = 2/3
			h3 = h3*2
			paths.append(1)
		else:
			x2 = x2*9
			h3 = h3*x2
			paths.append(2)
		if x >= 8:
			x = 0*x
			h3 = 8+x2
			paths.append(3)
		else:
			x2 = x2-h3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x2 = x**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))