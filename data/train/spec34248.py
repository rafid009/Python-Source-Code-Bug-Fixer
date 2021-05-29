import numpy as np 

def function(x):

	l8 = 6
	d0 = x
	x = x
	paths = []
	try:
		if d0 < 2:
			d0 = d0+l8
			d0 = 7/4
			paths.append(1)
		else:
			d0 = d0*d0
			x = d0+x
			l8 = 8-l8
			paths.append(2)
		if l8 > 1:
			l8 = 5+d0
			paths.append(3)
		else:
			l8 = x+3
			l8 = x+l8
			l8 = l8+9
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