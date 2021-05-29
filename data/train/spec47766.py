import numpy as np 

def function(x):

	x0 = 9
	h5 = 6
	paths = []
	try:
		if x0 > 6:
			h5 = h5-x
			h5 = h5+6
			h5 = h5-4
			paths.append(1)
		else:
			h5 = x0/h5
			x = x/2
			h5 = h5+3
			paths.append(2)
		if h5 >= 8:
			x = x*x
			h5 = h5+x0
			paths.append(3)
		else:
			h5 = h5*5
			h5 = h5+h5
			x = 4-x0
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		x = h5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))