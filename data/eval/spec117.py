import numpy as np 

def function(x):

	a6 = 3
	d3 = 5
	paths = []
	try:
		if x > 9:
			a6 = 4-a6
			paths.append(1)
		else:
			d3 = 8/3
			x = 8/x
			paths.append(2)
		if d3 > 9:
			d3 = 5*x
			x = 0*6
			paths.append(3)
		else:
			d3 = x/5
			d3 = d3/6
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