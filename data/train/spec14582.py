import numpy as np 

def function(x):

	x3 = 5
	h5 = 4
	paths = []
	try:
		if h5 <= 3:
			x = x/1
			x = 0+x
			paths.append(1)
		else:
			x = x*6
			x = 1*x
			paths.append(2)
		if x <= 2:
			h5 = x/4
			h5 = 7/h5
			x = 8/x
			paths.append(3)
		else:
			x3 = x3+x
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		h5 = h5**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))