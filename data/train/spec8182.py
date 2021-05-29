import numpy as np 

def function(x):

	v4 = x
	h6 = x
	paths = []
	try:
		if x >= 1:
			v4 = 3*x
			v4 = 7-v4
			h6 = h6*v4
			paths.append(1)
		else:
			x = x-5
			paths.append(2)
		if x < 1:
			x = 7-x
			paths.append(3)
		else:
			h6 = h6/3
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		v4 = h6**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))