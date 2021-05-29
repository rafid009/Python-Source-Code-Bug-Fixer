import numpy as np 

def function(x):

	h2 = 3
	e6 = 6
	paths = []
	try:
		if e6 <= 2:
			h2 = 8*1
			x = 1+x
			x = 6-h2
			paths.append(1)
		else:
			x = 9+x
			e6 = 8+e6
			paths.append(2)
		if x >= 2:
			e6 = e6*4
			x = x*1
			x = 5*x
			paths.append(3)
		else:
			h2 = 8/x
			h2 = h2+h2
			e6 = e6-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h2 = x**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))