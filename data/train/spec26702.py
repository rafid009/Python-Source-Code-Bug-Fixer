import numpy as np 

def function(x):

	n9 = 9
	g2 = 1
	paths = []
	try:
		if n9 > 0:
			g2 = g2/8
			paths.append(1)
		else:
			g2 = g2/1
			paths.append(2)
		if n9 < 0:
			g2 = x+0
			n9 = n9/4
			paths.append(3)
		else:
			n9 = n9+7
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