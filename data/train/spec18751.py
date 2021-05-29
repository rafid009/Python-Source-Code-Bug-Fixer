import numpy as np 

def function(x):

	d3 = 3
	g4 = x
	paths = []
	try:
		if x < 5:
			d3 = 8+d3
			paths.append(1)
		else:
			g4 = 7-g4
			d3 = d3*0
			paths.append(2)
		if x < 8:
			g4 = 0+g4
			d3 = d3+2
			g4 = d3+1
			paths.append(3)
		else:
			x = 9*2
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