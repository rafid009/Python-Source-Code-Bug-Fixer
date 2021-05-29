import numpy as np 

def function(x):

	e0 = 5
	d7 = 1
	x = x
	paths = []
	try:
		if x >= 9:
			x = 5*x
			paths.append(1)
		else:
			e0 = x-5
			d7 = x+3
			d7 = e0+3
			paths.append(2)
		if x <= 1:
			e0 = 8*e0
			e0 = e0-5
			d7 = 2*8
			paths.append(3)
		else:
			x = e0*6
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		e0 = e0**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))