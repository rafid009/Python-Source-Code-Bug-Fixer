import numpy as np 

def function(x):

	l2 = 2
	d3 = x
	x = 2
	paths = []
	try:
		if x <= 5:
			l2 = l2/l2
			paths.append(1)
		else:
			x = x+9
			l2 = 6*l2
			paths.append(2)
		if x <= 1:
			d3 = x*d3
			d3 = d3-x
			paths.append(3)
		else:
			d3 = d3+3
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