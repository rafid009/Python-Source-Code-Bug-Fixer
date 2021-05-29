import numpy as np 

def function(x):

	x4 = x
	g2 = 7
	paths = []
	try:
		if x < 6:
			x = x-3
			x4 = x4*2
			g2 = x/x4
			paths.append(1)
		else:
			g2 = g2+7
			g2 = g2+9
			paths.append(2)
		if g2 < 4:
			x4 = x*3
			paths.append(3)
		else:
			g2 = 7-x4
			g2 = 3+4
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		g2 = x4**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))