import numpy as np 

def function(x):

	d3 = 3
	i4 = 3
	paths = []
	try:
		if d3 > 5:
			d3 = d3/3
			i4 = d3-i4
			x = 7+0
			paths.append(1)
		else:
			i4 = i4-i4
			paths.append(2)
		if x >= 2:
			x = 0-2
			x = 4*i4
			d3 = 2-d3
			paths.append(3)
		else:
			x = d3*d3
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