import numpy as np 

def function(x):

	g2 = x
	o9 = x
	paths = []
	try:
		if o9 < 4:
			o9 = o9-2
			g2 = g2+1
			paths.append(1)
		else:
			g2 = g2+0
			paths.append(2)
		if o9 < 1:
			g2 = 3+g2
			g2 = x/g2
			o9 = o9+6
			paths.append(3)
		else:
			g2 = g2+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g2 = x**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))