import numpy as np 

def function(x):

	d2 = x
	d0 = 0
	paths = []
	try:
		if d2 <= 2:
			x = 9*x
			paths.append(1)
		else:
			d0 = 4*3
			x = 1+5
			paths.append(2)
		if d2 < 7:
			d0 = d0-4
			paths.append(3)
		else:
			d0 = d0/d0
			d0 = 0/d0
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		x = d0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))