import numpy as np 

def function(x):

	q8 = x
	d3 = x
	paths = []
	try:
		if x >= 8:
			d3 = 8-d3
			d3 = 9*q8
			q8 = q8/1
			paths.append(1)
		else:
			x = d3-2
			d3 = d3-1
			x = x*3
			paths.append(2)
		if d3 < 1:
			x = x/7
			paths.append(3)
		else:
			x = 0/x
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