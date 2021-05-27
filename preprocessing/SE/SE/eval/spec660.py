import numpy as np 

def function(x):

	h6 = 6
	v6 = 0
	x = x
	paths = []
	try:
		if x >= 2:
			x = 4+x
			x = x*6
			paths.append(1)
		else:
			h6 = h6*8
			paths.append(2)
		if v6 >= 1:
			x = 7/x
			x = h6-h6
			v6 = h6/v6
			paths.append(3)
		else:
			x = x+7
			h6 = h6*7
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