import numpy as np 

def function(x):

	d4 = 8
	b9 = x
	paths = []
	try:
		if d4 > 7:
			d4 = b9*d4
			paths.append(1)
		else:
			d4 = d4*4
			x = 0/x
			paths.append(2)
		if d4 < 2:
			x = x-6
			d4 = d4+d4
			paths.append(3)
		else:
			x = 2*x
			x = x*x
			x = 8/x
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