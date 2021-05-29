import numpy as np 

def function(x):

	o9 = x
	d0 = x
	paths = []
	try:
		if o9 < 4:
			d0 = 0+d0
			o9 = 1+2
			paths.append(1)
		else:
			x = 5*d0
			paths.append(2)
		if d0 > 1:
			x = x/x
			paths.append(3)
		else:
			d0 = 8-4
			d0 = d0-7
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