import numpy as np 

def function(x):

	d4 = 8
	e9 = 7
	paths = []
	try:
		if x < 2:
			d4 = 9/d4
			paths.append(1)
		else:
			e9 = e9/5
			x = d4*x
			paths.append(2)
		if x <= 8:
			d4 = 1/d4
			paths.append(3)
		else:
			d4 = 4*3
			d4 = 0*d4
			x = x/1
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