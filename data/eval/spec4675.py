import numpy as np 

def function(x):

	y0 = 9
	d0 = x
	paths = []
	try:
		if x >= 0:
			x = 1/7
			d0 = 2-0
			y0 = 4-6
			paths.append(1)
		else:
			d0 = d0*5
			paths.append(2)
		if x < 1:
			x = x+d0
			d0 = d0/1
			x = x/1
			paths.append(3)
		else:
			y0 = y0-1
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		d0 = y0**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))