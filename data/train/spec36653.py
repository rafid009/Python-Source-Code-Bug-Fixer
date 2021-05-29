import numpy as np 

def function(x):

	x0 = x
	d1 = x
	paths = []
	try:
		if x0 >= 2:
			x = 5*x
			d1 = x0*5
			paths.append(1)
		else:
			d1 = x*d1
			x = x+2
			d1 = d1-8
			paths.append(2)
		if d1 <= 2:
			x = 1*x
			x0 = x0-7
			paths.append(3)
		else:
			x0 = 8-x0
			x0 = 1+x0
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x0 = x0**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))