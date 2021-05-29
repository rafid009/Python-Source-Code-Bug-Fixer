import numpy as np 

def function(x):

	n4 = x
	d3 = x
	x = 8
	paths = []
	try:
		if d3 < 9:
			x = x/x
			x = 5+x
			n4 = d3*n4
			paths.append(1)
		else:
			d3 = 9/n4
			paths.append(2)
		if d3 <= 5:
			n4 = n4-3
			paths.append(3)
		else:
			x = x-x
			x = x-6
			x = x*x
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