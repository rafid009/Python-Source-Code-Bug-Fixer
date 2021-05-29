import numpy as np 

def function(x):

	a4 = x
	d3 = 8
	paths = []
	try:
		if a4 < 0:
			d3 = a4/d3
			a4 = 4+a4
			paths.append(1)
		else:
			a4 = 7+a4
			paths.append(2)
		if d3 > 3:
			d3 = 1*d3
			d3 = d3*9
			paths.append(3)
		else:
			a4 = 3*d3
			a4 = a4-2
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