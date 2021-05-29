import numpy as np 

def function(x):

	d3 = x
	d7 = 7
	paths = []
	try:
		if d7 > 1:
			d3 = 8+d3
			x = d3*1
			paths.append(1)
		else:
			d3 = d3*d7
			d7 = 9+d3
			paths.append(2)
		if d3 > 8:
			d3 = d3+x
			d7 = 5-d7
			paths.append(3)
		else:
			d3 = d3/d3
			d7 = x*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d7 = x**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))