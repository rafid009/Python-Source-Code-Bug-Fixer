import numpy as np 

def function(x):

	g8 = 4
	d3 = x
	paths = []
	try:
		if x < 7:
			d3 = 8/d3
			d3 = 5-1
			g8 = x+g8
			paths.append(1)
		else:
			d3 = d3/9
			g8 = g8+g8
			x = 7+7
			paths.append(2)
		if x <= 1:
			d3 = d3+x
			d3 = 4/d3
			g8 = 7-4
			paths.append(3)
		else:
			d3 = d3*x
			d3 = d3/6
			d3 = g8+d3
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		g8 = d3**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))