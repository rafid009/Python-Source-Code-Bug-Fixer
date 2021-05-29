import numpy as np 

def function(x):

	d0 = 8
	x3 = 0
	paths = []
	try:
		if d0 < 5:
			x = x*x
			x = 7-d0
			paths.append(1)
		else:
			x3 = 0*x3
			paths.append(2)
		if x3 < 1:
			x = x-6
			x3 = x3-x3
			x3 = 1-x3
			paths.append(3)
		else:
			x = x+x
			x = x+1
			x3 = x3*d0
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