import numpy as np 

def function(x):

	n4 = 8
	g2 = x
	paths = []
	try:
		if n4 > 3:
			g2 = 2-8
			g2 = g2+6
			paths.append(1)
		else:
			g2 = g2/n4
			g2 = n4/n4
			x = x+4
			paths.append(2)
		if g2 > 7:
			x = 7-3
			g2 = g2/g2
			paths.append(3)
		else:
			n4 = 2/n4
			n4 = 1*4
			x = 2/x
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