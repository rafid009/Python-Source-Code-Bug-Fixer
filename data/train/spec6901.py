import numpy as np 

def function(x):

	d3 = 3
	d0 = x
	paths = []
	try:
		if x >= 6:
			d3 = d3+0
			d3 = d3+4
			d3 = 7+x
			paths.append(1)
		else:
			x = x+3
			x = 5/2
			paths.append(2)
		if d3 < 1:
			d3 = 4-4
			d3 = d3*d3
			d3 = d3-x
			paths.append(3)
		else:
			d3 = 1-d3
			d3 = 6/d3
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		d0 = d0**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))