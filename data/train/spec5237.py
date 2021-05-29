import numpy as np 

def function(x):

	o9 = x
	d3 = x
	paths = []
	try:
		if d3 <= 9:
			o9 = 1/3
			paths.append(1)
		else:
			x = x+d3
			d3 = 8*d3
			paths.append(2)
		if x >= 6:
			x = 9+x
			d3 = d3+x
			d3 = 6/d3
			paths.append(3)
		else:
			o9 = o9*5
			o9 = 0-3
			o9 = x*9
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		x = d3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))