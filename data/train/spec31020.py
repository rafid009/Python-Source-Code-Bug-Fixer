import numpy as np 

def function(x):

	x8 = 1
	d3 = x
	paths = []
	try:
		if x8 > 0:
			d3 = d3*2
			x = x8/x
			paths.append(1)
		else:
			d3 = 7+d3
			d3 = x8/2
			paths.append(2)
		if d3 >= 1:
			d3 = d3+5
			paths.append(3)
		else:
			x = 6-x8
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