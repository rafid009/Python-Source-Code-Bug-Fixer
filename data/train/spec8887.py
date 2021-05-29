import numpy as np 

def function(x):

	e9 = x
	h8 = x
	paths = []
	try:
		if h8 < 1:
			h8 = h8*h8
			x = x*0
			x = x-9
			paths.append(1)
		else:
			h8 = x/e9
			e9 = 5/x
			h8 = 2*h8
			paths.append(2)
		if e9 > 9:
			e9 = e9/5
			e9 = 4*e9
			x = x*7
			paths.append(3)
		else:
			h8 = 0*e9
			e9 = e9-7
			e9 = 1-e9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h8 = x**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))