import numpy as np 

def function(x):

	l1 = x
	h5 = x
	paths = []
	try:
		if h5 < 5:
			l1 = l1*l1
			paths.append(1)
		else:
			h5 = h5/9
			l1 = h5*h5
			x = x*5
			paths.append(2)
		if x > 2:
			h5 = x*3
			h5 = h5*8
			paths.append(3)
		else:
			h5 = h5+3
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