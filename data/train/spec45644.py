import numpy as np 

def function(x):

	n8 = x
	d3 = 5
	paths = []
	try:
		if n8 <= 9:
			n8 = 3+n8
			paths.append(1)
		else:
			x = 8/x
			paths.append(2)
		if n8 >= 6:
			d3 = n8*d3
			paths.append(3)
		else:
			d3 = 6+d3
			x = 6*n8
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		n8 = n8**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))