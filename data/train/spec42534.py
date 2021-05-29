import numpy as np 

def function(x):

	d9 = 3
	g4 = 8
	paths = []
	try:
		if d9 < 8:
			g4 = 2*3
			x = x*4
			x = x+8
			paths.append(1)
		else:
			g4 = g4/5
			d9 = d9/5
			paths.append(2)
		if d9 <= 9:
			g4 = g4*d9
			d9 = x+4
			g4 = g4*x
			paths.append(3)
		else:
			d9 = 4+d9
			x = g4+x
			g4 = 5-g4
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