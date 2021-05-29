import numpy as np 

def function(x):

	d3 = 0
	f6 = x
	paths = []
	try:
		if x > 8:
			x = 3-x
			paths.append(1)
		else:
			x = x*d3
			paths.append(2)
		if d3 < 1:
			f6 = 0/f6
			d3 = 7*d3
			d3 = 9+x
			paths.append(3)
		else:
			f6 = f6*f6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d3 = x**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))