import numpy as np 

def function(x):

	i5 = x
	h5 = 0
	x = 6
	paths = []
	try:
		if h5 > 6:
			x = x+4
			paths.append(1)
		else:
			h5 = 6+h5
			paths.append(2)
		if h5 > 8:
			h5 = 1+h5
			h5 = h5+i5
			paths.append(3)
		else:
			h5 = 2+i5
			i5 = i5+9
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