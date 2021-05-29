import numpy as np 

def function(x):

	h1 = x
	d3 = 0
	paths = []
	try:
		if d3 <= 2:
			d3 = 3*3
			d3 = 6+5
			paths.append(1)
		else:
			x = x+d3
			x = 3+x
			paths.append(2)
		if x >= 9:
			h1 = h1*x
			paths.append(3)
		else:
			d3 = 6+d3
			h1 = h1*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d3 = x**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))