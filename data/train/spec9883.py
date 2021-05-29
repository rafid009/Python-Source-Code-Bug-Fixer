import numpy as np 

def function(x):

	t8 = x
	h6 = x
	x = 6
	paths = []
	try:
		if h6 < 4:
			h6 = 6/h6
			x = 3/x
			paths.append(1)
		else:
			h6 = x/h6
			paths.append(2)
		if h6 < 4:
			x = x+x
			paths.append(3)
		else:
			h6 = 7-h6
			x = 5*x
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		x = h6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))