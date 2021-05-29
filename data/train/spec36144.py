import numpy as np 

def function(x):

	p6 = 1
	d3 = x
	x = 2
	paths = []
	try:
		if x < 2:
			x = 1-x
			x = 1/2
			paths.append(1)
		else:
			x = d3/3
			d3 = x*5
			d3 = 9-d3
			paths.append(2)
		if d3 >= 2:
			x = 5-d3
			x = x/p6
			paths.append(3)
		else:
			d3 = p6/4
			x = x*6
			d3 = d3+p6
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