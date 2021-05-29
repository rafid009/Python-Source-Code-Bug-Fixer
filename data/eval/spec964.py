import numpy as np 

def function(x):

	h5 = x
	l6 = 9
	paths = []
	try:
		if l6 <= 0:
			l6 = l6-2
			l6 = 2*0
			h5 = h5-3
			paths.append(1)
		else:
			l6 = x+x
			paths.append(2)
		if h5 <= 3:
			h5 = 8+6
			l6 = l6+4
			h5 = h5*2
			paths.append(3)
		else:
			x = 0/9
			h5 = h5*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h5 = x**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))