import numpy as np 

def function(x):

	d0 = 3
	a7 = 2
	paths = []
	try:
		if x > 7:
			d0 = d0-5
			paths.append(1)
		else:
			a7 = x+3
			d0 = d0*6
			d0 = d0-3
			paths.append(2)
		if x <= 2:
			x = x-0
			d0 = x+d0
			a7 = a7-7
			paths.append(3)
		else:
			d0 = d0*d0
			x = a7/5
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		d0 = d0**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))