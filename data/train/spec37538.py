import numpy as np 

def function(x):

	d5 = 6
	l0 = 5
	x = 3
	paths = []
	try:
		if d5 < 1:
			x = 9-x
			paths.append(1)
		else:
			d5 = 1-3
			x = d5*x
			d5 = d5+d5
			paths.append(2)
		if x < 1:
			d5 = 7+x
			d5 = d5/4
			paths.append(3)
		else:
			d5 = d5-x
			d5 = x-4
			x = x/l0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d5 = x**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))