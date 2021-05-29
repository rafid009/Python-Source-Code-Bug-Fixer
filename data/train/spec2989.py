import numpy as np 

def function(x):

	n4 = x
	d3 = x
	paths = []
	try:
		if n4 <= 6:
			d3 = d3/5
			x = 3*x
			d3 = d3+9
			paths.append(1)
		else:
			n4 = 0-n4
			x = x*6
			paths.append(2)
		if n4 >= 2:
			d3 = d3+d3
			paths.append(3)
		else:
			d3 = 5*5
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		n4 = n4**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))