import numpy as np 

def function(x):

	d2 = x
	e0 = 8
	paths = []
	try:
		if e0 >= 8:
			e0 = 0*x
			paths.append(1)
		else:
			d2 = d2-4
			paths.append(2)
		if d2 >= 9:
			d2 = x/7
			e0 = e0-3
			paths.append(3)
		else:
			x = d2/9
			d2 = 6-0
			e0 = e0*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d2 = x**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))