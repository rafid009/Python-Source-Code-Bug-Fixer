import numpy as np 

def function(x):

	e6 = x
	h3 = 8
	x = x
	paths = []
	try:
		if h3 < 1:
			e6 = 1*x
			x = x*6
			e6 = x-0
			paths.append(1)
		else:
			x = 2*x
			paths.append(2)
		if e6 >= 9:
			h3 = 1-h3
			x = h3-h3
			paths.append(3)
		else:
			e6 = e6-h3
			h3 = h3*5
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		h3 = h3**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))