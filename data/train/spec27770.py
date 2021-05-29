import numpy as np 

def function(x):

	e0 = 6
	d0 = x
	paths = []
	try:
		if x <= 8:
			x = x+x
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if d0 > 7:
			d0 = d0*d0
			x = 0*x
			paths.append(3)
		else:
			d0 = 2+d0
			d0 = d0-e0
			d0 = e0/e0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e0 = x**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))