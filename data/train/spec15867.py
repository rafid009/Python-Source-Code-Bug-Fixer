import numpy as np 

def function(x):

	d7 = x
	n0 = 0
	x = x
	paths = []
	try:
		if n0 <= 3:
			x = d7*x
			d7 = d7*7
			paths.append(1)
		else:
			x = 7*x
			n0 = n0/n0
			n0 = n0/n0
			paths.append(2)
		if n0 <= 0:
			x = 0*x
			paths.append(3)
		else:
			n0 = n0/4
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		x = d7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))