import numpy as np 

def function(x):

	d0 = x
	y1 = x
	x = x
	paths = []
	try:
		if d0 >= 8:
			d0 = d0/2
			paths.append(1)
		else:
			d0 = d0+d0
			x = 0*x
			paths.append(2)
		if x >= 3:
			x = x/4
			paths.append(3)
		else:
			y1 = 7+2
			y1 = y1-8
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