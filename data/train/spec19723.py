import numpy as np 

def function(x):

	h7 = x
	e2 = 6
	paths = []
	try:
		if h7 < 0:
			x = 0-x
			h7 = h7-h7
			paths.append(1)
		else:
			e2 = 5*e2
			x = e2*e2
			h7 = 1-h7
			paths.append(2)
		if h7 >= 3:
			x = 5*7
			h7 = x-4
			e2 = e2*6
			paths.append(3)
		else:
			e2 = 4*7
			e2 = 7-8
			e2 = 0+1
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		e2 = h7**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))