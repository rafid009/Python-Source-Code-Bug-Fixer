import numpy as np 

def function(x):

	g2 = x
	n0 = 1
	paths = []
	try:
		if g2 < 2:
			g2 = g2/n0
			paths.append(1)
		else:
			n0 = n0-g2
			n0 = n0+3
			g2 = 2*g2
			paths.append(2)
		if n0 >= 3:
			n0 = n0/6
			x = 7+2
			paths.append(3)
		else:
			n0 = g2-n0
			g2 = 3+7
			x = x*2
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		g2 = n0**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))