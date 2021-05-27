import numpy as np 

def function(x):

	g2 = x
	a6 = 2
	paths = []
	try:
		if a6 > 3:
			g2 = 1*g2
			paths.append(1)
		else:
			a6 = a6-g2
			paths.append(2)
		if x <= 5:
			g2 = g2-1
			g2 = 0*g2
			paths.append(3)
		else:
			g2 = 5+5
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