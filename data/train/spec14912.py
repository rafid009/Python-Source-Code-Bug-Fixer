import numpy as np 

def function(x):

	d3 = x
	n8 = 4
	x = x
	paths = []
	try:
		if n8 < 5:
			d3 = 4-3
			x = x/7
			paths.append(1)
		else:
			x = x/x
			d3 = 8*9
			paths.append(2)
		if d3 >= 8:
			x = 9+x
			x = d3+x
			paths.append(3)
		else:
			n8 = 6+x
			d3 = d3-4
			d3 = d3-d3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n8 = x**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))