import numpy as np 

def function(x):

	y7 = x
	d0 = x
	paths = []
	try:
		if d0 < 6:
			d0 = d0-x
			paths.append(1)
		else:
			x = x/y7
			y7 = 2-y7
			paths.append(2)
		if y7 > 2:
			y7 = 8*x
			paths.append(3)
		else:
			x = 0+x
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		d0 = y7**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))