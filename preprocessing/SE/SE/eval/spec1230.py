import numpy as np 

def function(x):

	d3 = 7
	g3 = x
	paths = []
	try:
		if x > 7:
			d3 = d3+d3
			x = x/g3
			x = x/d3
			paths.append(1)
		else:
			g3 = g3+7
			paths.append(2)
		if x > 5:
			x = 9-x
			g3 = x-x
			paths.append(3)
		else:
			d3 = 1-9
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