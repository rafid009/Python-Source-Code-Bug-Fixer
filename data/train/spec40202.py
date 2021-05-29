import numpy as np 

def function(x):

	n8 = x
	g2 = x
	paths = []
	try:
		if n8 >= 4:
			n8 = n8+8
			g2 = g2*g2
			x = g2/7
			paths.append(1)
		else:
			n8 = n8*n8
			x = 4/6
			paths.append(2)
		if n8 >= 4:
			g2 = 3-g2
			paths.append(3)
		else:
			x = g2+1
			n8 = 2+n8
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