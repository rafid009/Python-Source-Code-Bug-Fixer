import numpy as np 

def function(x):

	k4 = x
	d0 = 1
	paths = []
	try:
		if x > 6:
			k4 = k4*6
			k4 = 6/x
			paths.append(1)
		else:
			d0 = d0+0
			paths.append(2)
		if x < 2:
			d0 = d0-0
			x = x*1
			d0 = x/3
			paths.append(3)
		else:
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))