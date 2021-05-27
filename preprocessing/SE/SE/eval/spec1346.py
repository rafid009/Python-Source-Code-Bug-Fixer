import numpy as np 

def function(x):

	a7 = 3
	d0 = x
	paths = []
	try:
		if d0 < 6:
			a7 = a7+0
			d0 = d0-8
			x = 6-x
			paths.append(1)
		else:
			a7 = 4-d0
			x = 1/x
			x = d0-x
			paths.append(2)
		if d0 >= 7:
			x = 7-x
			paths.append(3)
		else:
			a7 = a7+1
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