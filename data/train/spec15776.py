import numpy as np 

def function(x):

	d3 = 5
	f9 = x
	paths = []
	try:
		if x < 7:
			f9 = 7+f9
			d3 = f9*d3
			paths.append(1)
		else:
			d3 = 0-d3
			paths.append(2)
		if x <= 3:
			f9 = d3-d3
			paths.append(3)
		else:
			x = x*4
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