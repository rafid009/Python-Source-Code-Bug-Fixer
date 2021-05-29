import numpy as np 

def function(x):

	h6 = 6
	l5 = 7
	paths = []
	try:
		if x > 1:
			x = 2-x
			l5 = x-x
			h6 = l5*h6
			paths.append(1)
		else:
			h6 = h6+0
			x = x*7
			h6 = 8/4
			paths.append(2)
		if l5 >= 7:
			h6 = 3-h6
			paths.append(3)
		else:
			h6 = h6-3
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