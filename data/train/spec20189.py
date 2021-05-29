import numpy as np 

def function(x):

	d3 = 2
	g3 = 4
	x = x
	paths = []
	try:
		if g3 > 8:
			g3 = d3*0
			d3 = g3*8
			g3 = 5+g3
			paths.append(1)
		else:
			x = 3-4
			d3 = d3+2
			g3 = g3+9
			paths.append(2)
		if d3 < 2:
			d3 = d3*3
			paths.append(3)
		else:
			x = x+x
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