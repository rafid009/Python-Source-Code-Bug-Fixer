import numpy as np 

def function(x):

	e2 = 2
	h4 = x
	paths = []
	try:
		if h4 >= 2:
			h4 = 2/8
			x = e2*8
			e2 = e2*1
			paths.append(1)
		else:
			h4 = 0+h4
			e2 = e2+3
			e2 = 7/e2
			paths.append(2)
		if x > 7:
			h4 = h4-e2
			paths.append(3)
		else:
			h4 = 5-h4
			e2 = 9+0
			e2 = x-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h4 = x**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))