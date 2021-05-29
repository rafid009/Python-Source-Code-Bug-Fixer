import numpy as np 

def function(x):

	d3 = x
	n3 = x
	paths = []
	try:
		if x < 7:
			n3 = 2*n3
			paths.append(1)
		else:
			d3 = 9*d3
			x = 5+6
			paths.append(2)
		if x > 5:
			x = x*x
			x = 3/x
			d3 = n3/x
			paths.append(3)
		else:
			x = 5/x
			n3 = x-3
			n3 = 9+n3
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		n3 = n3**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))