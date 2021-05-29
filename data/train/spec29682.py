import numpy as np 

def function(x):

	k6 = 4
	h9 = x
	paths = []
	try:
		if x >= 2:
			k6 = 2+k6
			h9 = h9*6
			paths.append(1)
		else:
			x = x/6
			x = 9/x
			paths.append(2)
		if x >= 5:
			h9 = k6-8
			x = h9*x
			x = 4*x
			paths.append(3)
		else:
			x = x-6
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