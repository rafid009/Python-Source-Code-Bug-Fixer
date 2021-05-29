import numpy as np 

def function(x):

	d0 = 7
	y2 = x
	x = x
	paths = []
	try:
		if y2 < 9:
			x = 4*2
			x = x/d0
			y2 = x*y2
			paths.append(1)
		else:
			x = x-x
			d0 = x*d0
			d0 = y2/6
			paths.append(2)
		if d0 >= 5:
			d0 = d0*y2
			x = 9+2
			d0 = d0-4
			paths.append(3)
		else:
			y2 = d0/y2
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