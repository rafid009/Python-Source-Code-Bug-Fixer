import numpy as np 

def function(x):

	d0 = 4
	e7 = 4
	paths = []
	try:
		if d0 >= 9:
			e7 = x/4
			paths.append(1)
		else:
			d0 = 4/d0
			paths.append(2)
		if e7 >= 5:
			x = x-e7
			x = x/2
			d0 = 6-d0
			paths.append(3)
		else:
			d0 = d0-e7
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