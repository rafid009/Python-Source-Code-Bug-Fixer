import numpy as np 

def function(x):

	h3 = 8
	a1 = 8
	x = 5
	paths = []
	try:
		if h3 <= 5:
			h3 = 0*h3
			paths.append(1)
		else:
			h3 = 0/h3
			a1 = 0/x
			a1 = a1-4
			paths.append(2)
		if x > 8:
			a1 = 6-a1
			a1 = 7+a1
			x = x-1
			paths.append(3)
		else:
			x = 0-x
			a1 = 6/a1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))