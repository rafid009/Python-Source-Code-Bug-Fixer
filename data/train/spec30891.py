import numpy as np 

def function(x):

	h5 = x
	j4 = x
	paths = []
	try:
		if x < 1:
			x = h5*j4
			x = h5/j4
			h5 = 7-x
			paths.append(1)
		else:
			j4 = 2*j4
			paths.append(2)
		if j4 <= 8:
			x = j4*7
			h5 = 1+7
			x = j4*3
			paths.append(3)
		else:
			x = h5-6
			x = x-1
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