import numpy as np 

def function(x):

	n7 = 5
	d0 = x
	paths = []
	try:
		if d0 < 7:
			d0 = d0-6
			d0 = d0*6
			d0 = d0-4
			paths.append(1)
		else:
			n7 = x*n7
			x = 3*n7
			n7 = n7+d0
			paths.append(2)
		if d0 > 1:
			d0 = x+x
			d0 = d0+2
			paths.append(3)
		else:
			n7 = 8-4
			x = 3/x
			n7 = 4*d0
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