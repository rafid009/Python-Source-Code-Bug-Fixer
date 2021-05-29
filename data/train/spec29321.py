import numpy as np 

def function(x):

	d0 = x
	x4 = 1
	paths = []
	try:
		if x4 >= 7:
			x4 = x4-x4
			d0 = 2/8
			x = 3*x
			paths.append(1)
		else:
			d0 = 5*d0
			x4 = 7*x
			x = x4/8
			paths.append(2)
		if x4 <= 7:
			x4 = x4/8
			paths.append(3)
		else:
			d0 = d0*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d0 = x**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))