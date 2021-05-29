import numpy as np 

def function(x):

	d5 = x
	x0 = x
	paths = []
	try:
		if d5 >= 0:
			x = x-5
			paths.append(1)
		else:
			x = 8+0
			x0 = x0*2
			paths.append(2)
		if x0 >= 0:
			x0 = 0-3
			x = 9*4
			paths.append(3)
		else:
			d5 = d5-5
			x = 8*x0
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