import numpy as np 

def function(x):

	e2 = 8
	h3 = 0
	x = x
	paths = []
	try:
		if x < 8:
			e2 = e2-x
			e2 = x*0
			h3 = 2*h3
			paths.append(1)
		else:
			h3 = x/8
			paths.append(2)
		if h3 >= 4:
			h3 = h3/3
			paths.append(3)
		else:
			e2 = h3*h3
			x = 5/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h3 = x**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))