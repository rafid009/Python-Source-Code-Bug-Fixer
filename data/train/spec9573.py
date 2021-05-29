import numpy as np 

def function(x):

	y4 = x
	d3 = x
	paths = []
	try:
		if y4 <= 1:
			x = x-d3
			y4 = y4+3
			paths.append(1)
		else:
			y4 = y4+2
			y4 = 0-y4
			y4 = y4/4
			paths.append(2)
		if y4 >= 8:
			y4 = d3*8
			paths.append(3)
		else:
			y4 = 0/y4
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