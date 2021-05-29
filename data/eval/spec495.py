import numpy as np 

def function(x):

	d6 = x
	d4 = 6
	paths = []
	try:
		if d6 < 1:
			x = 5*x
			d4 = d4*d6
			d4 = 5/d4
			paths.append(1)
		else:
			d6 = 5+d6
			x = x-x
			paths.append(2)
		if x > 1:
			x = x-d6
			x = x*x
			paths.append(3)
		else:
			x = x+2
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