import numpy as np 

def function(x):

	d0 = x
	e9 = 8
	paths = []
	try:
		if x > 3:
			e9 = e9-2
			e9 = e9-5
			x = 2*x
			paths.append(1)
		else:
			x = 4+x
			x = x/d0
			d0 = d0*d0
			paths.append(2)
		if d0 <= 1:
			x = x*9
			e9 = 8*e9
			d0 = d0-x
			paths.append(3)
		else:
			x = 8+8
			d0 = d0/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e9 = x**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))