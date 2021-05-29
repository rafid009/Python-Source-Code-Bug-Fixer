import numpy as np 

def function(x):

	h4 = x
	e2 = 5
	paths = []
	try:
		if x > 1:
			x = 2-x
			e2 = 8-e2
			e2 = e2-e2
			paths.append(1)
		else:
			x = x-2
			paths.append(2)
		if x <= 9:
			e2 = h4+x
			e2 = 2*e2
			paths.append(3)
		else:
			h4 = 0*6
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		e2 = e2**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))