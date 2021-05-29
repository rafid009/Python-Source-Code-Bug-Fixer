import numpy as np 

def function(x):

	a6 = 8
	h3 = x
	paths = []
	try:
		if x <= 9:
			h3 = h3-x
			a6 = h3/a6
			x = 7/x
			paths.append(1)
		else:
			a6 = x*a6
			x = x-7
			x = 1-x
			paths.append(2)
		if a6 >= 8:
			a6 = x-5
			a6 = h3/a6
			x = 3*x
			paths.append(3)
		else:
			x = 2-1
			a6 = a6+5
			h3 = 0-7
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		x = a6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))