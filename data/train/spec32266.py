import numpy as np 

def function(x):

	g2 = x
	u9 = 8
	paths = []
	try:
		if x <= 0:
			g2 = x-x
			x = x-0
			paths.append(1)
		else:
			x = 8-x
			paths.append(2)
		if x >= 6:
			u9 = u9/1
			x = x+8
			paths.append(3)
		else:
			g2 = g2*1
			u9 = u9-7
			g2 = x-0
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