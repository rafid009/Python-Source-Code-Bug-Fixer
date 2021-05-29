import numpy as np 

def function(x):

	d3 = 7
	g4 = 7
	x = x
	paths = []
	try:
		if x > 6:
			g4 = g4*x
			d3 = d3+g4
			d3 = x+5
			paths.append(1)
		else:
			d3 = g4-4
			paths.append(2)
		if g4 < 8:
			g4 = g4+1
			x = x*3
			paths.append(3)
		else:
			x = 0*0
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