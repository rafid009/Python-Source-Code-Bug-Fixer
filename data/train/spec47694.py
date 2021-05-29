import numpy as np 

def function(x):

	y8 = 9
	d0 = 5
	paths = []
	try:
		if y8 <= 6:
			x = d0/9
			x = y8/7
			paths.append(1)
		else:
			d0 = 2+d0
			y8 = y8/y8
			paths.append(2)
		if y8 <= 1:
			x = x-2
			d0 = d0*x
			paths.append(3)
		else:
			y8 = x/x
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