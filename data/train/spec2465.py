import numpy as np 

def function(x):

	x0 = 8
	g2 = 1
	paths = []
	try:
		if x0 > 1:
			x = x-3
			paths.append(1)
		else:
			x0 = x0/4
			g2 = g2-2
			x = x0/8
			paths.append(2)
		if g2 >= 1:
			x0 = 4-0
			x = x/8
			paths.append(3)
		else:
			g2 = g2+2
			g2 = g2-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x0 = x**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))