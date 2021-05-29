import numpy as np 

def function(x):

	y7 = x
	d3 = x
	paths = []
	try:
		if y7 >= 3:
			d3 = d3*3
			d3 = y7+y7
			paths.append(1)
		else:
			x = 5+x
			d3 = d3*6
			paths.append(2)
		if x >= 0:
			d3 = x+9
			y7 = y7+6
			d3 = 8+d3
			paths.append(3)
		else:
			x = d3+6
			x = 0-x
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