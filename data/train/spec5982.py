import numpy as np 

def function(x):

	d3 = x
	y8 = x
	paths = []
	try:
		if x <= 5:
			x = 0-y8
			paths.append(1)
		else:
			y8 = y8*2
			d3 = d3+3
			d3 = 5*d3
			paths.append(2)
		if d3 >= 7:
			x = x-0
			d3 = d3-4
			paths.append(3)
		else:
			x = 7+x
			x = x-6
			x = 8/x
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