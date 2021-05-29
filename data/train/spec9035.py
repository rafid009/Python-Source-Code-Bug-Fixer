import numpy as np 

def function(x):

	z9 = 5
	d3 = 4
	paths = []
	try:
		if x > 0:
			d3 = 7/d3
			x = x*7
			paths.append(1)
		else:
			d3 = d3*x
			d3 = d3+1
			paths.append(2)
		if d3 < 0:
			z9 = z9-d3
			paths.append(3)
		else:
			d3 = 0-d3
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		z9 = d3**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))