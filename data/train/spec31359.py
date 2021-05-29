import numpy as np 

def function(x):

	d3 = 2
	d8 = 3
	paths = []
	try:
		if d3 > 9:
			x = x+6
			d3 = d3+d8
			d3 = 8+d3
			paths.append(1)
		else:
			x = 4/x
			d3 = d3-8
			paths.append(2)
		if x < 9:
			d8 = d8-3
			x = x+x
			paths.append(3)
		else:
			x = 3-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d8 = x**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))