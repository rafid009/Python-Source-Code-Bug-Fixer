import numpy as np 

def function(x):

	a4 = x
	d3 = x
	paths = []
	try:
		if d3 < 3:
			a4 = a4-1
			d3 = 3+0
			paths.append(1)
		else:
			d3 = x+d3
			x = x/a4
			d3 = d3+4
			paths.append(2)
		if d3 < 3:
			x = 5+4
			x = x+x
			paths.append(3)
		else:
			a4 = d3+a4
			d3 = d3-x
			x = 2-a4
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