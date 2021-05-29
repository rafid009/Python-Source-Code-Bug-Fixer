import numpy as np 

def function(x):

	y8 = 9
	d3 = 8
	x = x
	paths = []
	try:
		if d3 <= 8:
			d3 = d3/y8
			paths.append(1)
		else:
			d3 = d3-9
			y8 = 7+y8
			paths.append(2)
		if d3 <= 1:
			d3 = d3-1
			paths.append(3)
		else:
			d3 = d3/4
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		x = d3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))