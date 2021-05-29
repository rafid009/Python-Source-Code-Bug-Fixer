import numpy as np 

def function(x):

	n9 = 2
	g2 = x
	paths = []
	try:
		if n9 > 4:
			x = x/4
			x = x*4
			paths.append(1)
		else:
			x = 9+x
			n9 = n9*2
			paths.append(2)
		if g2 <= 7:
			n9 = n9-3
			g2 = g2/g2
			paths.append(3)
		else:
			n9 = n9/x
			x = 3+n9
			g2 = g2-g2
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