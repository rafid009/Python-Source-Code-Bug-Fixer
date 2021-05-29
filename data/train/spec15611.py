import numpy as np 

def function(x):

	l5 = x
	d3 = 2
	paths = []
	try:
		if x > 5:
			x = 5+x
			d3 = d3/x
			paths.append(1)
		else:
			x = x-d3
			paths.append(2)
		if d3 <= 3:
			d3 = d3/l5
			paths.append(3)
		else:
			l5 = l5*4
			d3 = 5+d3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))