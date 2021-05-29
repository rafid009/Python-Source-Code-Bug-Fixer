import numpy as np 

def function(x):

	d3 = x
	o9 = 3
	paths = []
	try:
		if d3 <= 5:
			d3 = 6*d3
			x = x+8
			paths.append(1)
		else:
			d3 = 2*x
			o9 = x-o9
			paths.append(2)
		if d3 > 8:
			d3 = x+d3
			d3 = 2/d3
			paths.append(3)
		else:
			x = 9-x
			x = x/8
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