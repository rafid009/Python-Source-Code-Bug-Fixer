import numpy as np 

def function(x):

	d3 = x
	d2 = 6
	paths = []
	try:
		if x <= 8:
			x = x*2
			x = x/d3
			d3 = 6-d3
			paths.append(1)
		else:
			d3 = 4+d3
			d3 = 8+x
			paths.append(2)
		if x <= 8:
			d2 = 3-7
			d3 = d3*7
			d3 = 5-d3
			paths.append(3)
		else:
			d3 = d3+6
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		x = d2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))