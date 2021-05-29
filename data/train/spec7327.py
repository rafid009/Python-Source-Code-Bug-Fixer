import numpy as np 

def function(x):

	n8 = 2
	h5 = x
	paths = []
	try:
		if x < 8:
			x = h5*n8
			x = x+6
			h5 = h5+n8
			paths.append(1)
		else:
			n8 = n8-h5
			x = x-8
			x = 1+x
			paths.append(2)
		if h5 <= 7:
			x = 3+5
			paths.append(3)
		else:
			n8 = 1*n8
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		x = n8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))