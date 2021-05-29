import numpy as np 

def function(x):

	h1 = 9
	e2 = x
	paths = []
	try:
		if x > 2:
			h1 = h1+7
			x = 8+h1
			h1 = 9+h1
			paths.append(1)
		else:
			x = x+h1
			h1 = 2-h1
			h1 = 9+h1
			paths.append(2)
		if x >= 0:
			e2 = e2*e2
			x = x-6
			x = 0*x
			paths.append(3)
		else:
			x = x*1
			h1 = 3/x
			e2 = e2-6
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		h1 = e2**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))