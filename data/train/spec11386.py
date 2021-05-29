import numpy as np 

def function(x):

	d4 = x
	l8 = 2
	paths = []
	try:
		if x >= 9:
			x = x+l8
			paths.append(1)
		else:
			l8 = l8/6
			paths.append(2)
		if l8 >= 6:
			d4 = d4+3
			x = 8*2
			d4 = 3-x
			paths.append(3)
		else:
			l8 = 0*d4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d4 = x**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))