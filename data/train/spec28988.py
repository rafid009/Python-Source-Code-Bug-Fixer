import numpy as np 

def function(x):

	h5 = 7
	e6 = x
	paths = []
	try:
		if h5 < 2:
			h5 = 9*6
			e6 = 3+5
			h5 = 6*x
			paths.append(1)
		else:
			e6 = e6/e6
			paths.append(2)
		if h5 < 2:
			h5 = h5/5
			paths.append(3)
		else:
			e6 = e6+1
			h5 = 7+x
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