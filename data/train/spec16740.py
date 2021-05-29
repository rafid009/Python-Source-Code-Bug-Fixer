import numpy as np 

def function(x):

	d3 = 0
	e4 = x
	paths = []
	try:
		if x >= 2:
			d3 = d3*9
			paths.append(1)
		else:
			d3 = d3*9
			e4 = e4-x
			paths.append(2)
		if e4 >= 2:
			x = 5+d3
			d3 = d3-e4
			paths.append(3)
		else:
			x = 4-x
			e4 = 9*e4
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		e4 = d3**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))