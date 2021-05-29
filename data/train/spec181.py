import numpy as np 

def function(x):

	d3 = x
	y5 = 8
	paths = []
	try:
		if d3 >= 1:
			x = x+4
			y5 = 7-0
			x = 4*9
			paths.append(1)
		else:
			x = 4*x
			y5 = y5*3
			paths.append(2)
		if y5 <= 8:
			d3 = 8/d3
			paths.append(3)
		else:
			d3 = d3+x
			x = 5+x
			d3 = d3-4
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		y5 = d3**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))