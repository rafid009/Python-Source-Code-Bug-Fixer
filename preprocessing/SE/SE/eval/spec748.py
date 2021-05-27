import numpy as np 

def function(x):

	d3 = 4
	k4 = 2
	paths = []
	try:
		if x > 1:
			d3 = d3-9
			paths.append(1)
		else:
			d3 = d3-3
			paths.append(2)
		if k4 < 9:
			k4 = 5/d3
			paths.append(3)
		else:
			k4 = d3-k4
			k4 = k4/9
			d3 = d3+0
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