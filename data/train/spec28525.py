import numpy as np 

def function(x):

	l0 = x
	d3 = 5
	paths = []
	try:
		if d3 < 6:
			l0 = 9-l0
			paths.append(1)
		else:
			l0 = l0*7
			paths.append(2)
		if l0 < 1:
			d3 = d3-0
			l0 = l0/6
			d3 = l0-l0
			paths.append(3)
		else:
			d3 = d3*4
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		l0 = l0**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))