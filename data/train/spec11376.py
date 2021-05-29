import numpy as np 

def function(x):

	g2 = x
	e1 = x
	paths = []
	try:
		if e1 < 3:
			e1 = x-3
			paths.append(1)
		else:
			e1 = e1+3
			e1 = e1*7
			paths.append(2)
		if e1 >= 8:
			x = e1*x
			x = 0-x
			paths.append(3)
		else:
			g2 = 9-3
			g2 = g2*7
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		g2 = e1**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))