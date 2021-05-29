import numpy as np 

def function(x):

	h5 = 6
	i6 = 5
	paths = []
	try:
		if h5 > 7:
			i6 = 5-i6
			h5 = h5-h5
			paths.append(1)
		else:
			i6 = h5-i6
			paths.append(2)
		if i6 >= 6:
			h5 = h5*1
			h5 = 9/2
			paths.append(3)
		else:
			h5 = 9/i6
			x = x*h5
			h5 = 2/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i6 = x**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))