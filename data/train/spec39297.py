import numpy as np 

def function(x):

	l5 = x
	d3 = x
	paths = []
	try:
		if x >= 3:
			x = x+6
			paths.append(1)
		else:
			x = 9+d3
			paths.append(2)
		if x < 1:
			l5 = l5+x
			l5 = l5/x
			l5 = l5-7
			paths.append(3)
		else:
			d3 = d3*x
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