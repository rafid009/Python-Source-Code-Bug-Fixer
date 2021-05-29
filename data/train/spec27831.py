import numpy as np 

def function(x):

	d3 = x
	w1 = 3
	paths = []
	try:
		if d3 <= 1:
			d3 = 4/d3
			x = 1*d3
			w1 = w1-w1
			paths.append(1)
		else:
			d3 = 7+d3
			paths.append(2)
		if d3 <= 8:
			d3 = d3+6
			d3 = w1+x
			paths.append(3)
		else:
			w1 = d3*w1
			x = 3-w1
			x = d3-x
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