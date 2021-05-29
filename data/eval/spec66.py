import numpy as np 

def function(x):

	d0 = x
	d3 = 8
	paths = []
	try:
		if d3 <= 9:
			x = x+3
			x = x/1
			paths.append(1)
		else:
			d3 = d3-2
			paths.append(2)
		if d0 >= 8:
			d3 = d3-d0
			x = x-d3
			paths.append(3)
		else:
			x = d3/x
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		d3 = d0**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))