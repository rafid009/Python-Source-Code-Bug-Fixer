import numpy as np 

def function(x):

	e5 = 2
	d9 = x
	paths = []
	try:
		if x <= 4:
			d9 = 1*d9
			paths.append(1)
		else:
			e5 = e5*e5
			d9 = d9-8
			paths.append(2)
		if x >= 1:
			d9 = 0*8
			paths.append(3)
		else:
			e5 = e5*7
			x = x-8
			x = x*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e5 = x**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))