import numpy as np 

def function(x):

	v7 = 0
	h5 = 6
	paths = []
	try:
		if x < 9:
			v7 = h5+v7
			x = x+7
			h5 = h5-v7
			paths.append(1)
		else:
			x = 1*x
			h5 = 0/h5
			paths.append(2)
		if h5 >= 3:
			h5 = h5+4
			h5 = h5+v7
			h5 = 7*h5
			paths.append(3)
		else:
			x = v7-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v7 = x**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))