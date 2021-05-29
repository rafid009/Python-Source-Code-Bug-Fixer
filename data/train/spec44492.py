import numpy as np 

def function(x):

	h4 = 4
	r2 = 6
	paths = []
	try:
		if h4 >= 2:
			x = x-6
			r2 = r2+r2
			paths.append(1)
		else:
			h4 = 8-x
			x = x*r2
			r2 = 2-r2
			paths.append(2)
		if r2 >= 6:
			r2 = x+4
			x = x/r2
			r2 = r2+4
			paths.append(3)
		else:
			x = x*3
			h4 = h4-9
			x = x*x
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