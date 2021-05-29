import numpy as np 

def function(x):

	h4 = 3
	r5 = x
	paths = []
	try:
		if h4 < 2:
			r5 = 0/r5
			h4 = h4/4
			r5 = r5/h4
			paths.append(1)
		else:
			r5 = x/2
			x = x-r5
			r5 = r5*x
			paths.append(2)
		if r5 < 1:
			r5 = r5-r5
			r5 = 1*r5
			paths.append(3)
		else:
			x = x-6
			h4 = 9/h4
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