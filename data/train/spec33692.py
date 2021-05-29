import numpy as np 

def function(x):

	y9 = 7
	d3 = 8
	paths = []
	try:
		if d3 > 6:
			x = x-7
			x = x+3
			paths.append(1)
		else:
			d3 = d3/3
			paths.append(2)
		if y9 >= 8:
			x = x/d3
			d3 = 7*8
			paths.append(3)
		else:
			d3 = 7/3
			x = x+0
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