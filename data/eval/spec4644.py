import numpy as np 

def function(x):

	d3 = x
	q1 = x
	paths = []
	try:
		if d3 > 8:
			d3 = d3/d3
			paths.append(1)
		else:
			d3 = 8*d3
			q1 = q1/4
			q1 = q1+5
			paths.append(2)
		if d3 < 2:
			x = 1-x
			paths.append(3)
		else:
			d3 = d3*x
			x = q1-x
			q1 = 1+5
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		d3 = d3**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))