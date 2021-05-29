import numpy as np 

def function(x):

	d0 = 3
	a7 = x
	paths = []
	try:
		if x > 2:
			a7 = a7+x
			d0 = d0/5
			d0 = d0*x
			paths.append(1)
		else:
			x = x-8
			d0 = 1*d0
			paths.append(2)
		if a7 > 4:
			d0 = d0*7
			paths.append(3)
		else:
			a7 = a7/5
			d0 = 5+x
			x = 2/x
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