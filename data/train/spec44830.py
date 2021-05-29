import numpy as np 

def function(x):

	g2 = x
	d3 = x
	paths = []
	try:
		if g2 < 6:
			d3 = 7+d3
			d3 = 3+d3
			paths.append(1)
		else:
			d3 = x*6
			x = 3/x
			paths.append(2)
		if x > 5:
			x = g2*5
			d3 = d3-d3
			paths.append(3)
		else:
			g2 = g2/g2
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