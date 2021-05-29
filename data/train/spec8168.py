import numpy as np 

def function(x):

	d3 = 9
	h2 = x
	paths = []
	try:
		if x > 0:
			h2 = h2/h2
			h2 = h2/2
			paths.append(1)
		else:
			d3 = 9-d3
			paths.append(2)
		if d3 >= 6:
			d3 = 0-d3
			paths.append(3)
		else:
			d3 = 6+x
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