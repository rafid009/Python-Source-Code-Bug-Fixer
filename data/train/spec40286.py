import numpy as np 

def function(x):

	e2 = x
	h0 = x
	paths = []
	try:
		if e2 >= 1:
			x = x-7
			e2 = e2*h0
			e2 = 7*e2
			paths.append(1)
		else:
			h0 = x/h0
			paths.append(2)
		if h0 > 2:
			e2 = 2/e2
			x = 0/x
			paths.append(3)
		else:
			e2 = 3-e2
			e2 = 6/e2
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		x = e2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))