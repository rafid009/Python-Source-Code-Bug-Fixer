import numpy as np 

def function(x):

	a2 = 3
	h6 = 2
	paths = []
	try:
		if x >= 0:
			h6 = 5/x
			h6 = h6/h6
			a2 = a2/x
			paths.append(1)
		else:
			h6 = a2+8
			a2 = h6-x
			a2 = h6+a2
			paths.append(2)
		if x >= 0:
			x = x-x
			a2 = 0+a2
			paths.append(3)
		else:
			h6 = h6*3
			a2 = a2-9
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a2 = x**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))