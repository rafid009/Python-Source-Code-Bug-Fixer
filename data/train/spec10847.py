import numpy as np 

def function(x):

	e7 = 3
	d3 = 7
	paths = []
	try:
		if x > 0:
			d3 = x*x
			d3 = 4*2
			paths.append(1)
		else:
			e7 = e7-d3
			paths.append(2)
		if x >= 7:
			x = x*3
			paths.append(3)
		else:
			e7 = 1-d3
			d3 = d3/x
			e7 = e7/6
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		d3 = e7**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))