import numpy as np 

def function(x):

	n0 = 8
	d3 = 0
	x = x
	paths = []
	try:
		if x > 0:
			n0 = d3-x
			paths.append(1)
		else:
			d3 = d3+d3
			paths.append(2)
		if x >= 8:
			x = x-6
			n0 = 5/2
			paths.append(3)
		else:
			d3 = 5-0
			x = x*3
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		n0 = n0**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))