import numpy as np 

def function(x):

	h5 = x
	l5 = 0
	paths = []
	try:
		if h5 > 9:
			h5 = h5+5
			h5 = h5+8
			x = x-l5
			paths.append(1)
		else:
			l5 = x*l5
			x = l5-h5
			x = 1-x
			paths.append(2)
		if x < 3:
			x = x-8
			paths.append(3)
		else:
			x = 3+9
			h5 = 6+9
			h5 = h5/h5
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