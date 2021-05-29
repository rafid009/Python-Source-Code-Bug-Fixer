import numpy as np 

def function(x):

	a9 = x
	g2 = 2
	paths = []
	try:
		if x >= 4:
			x = x/6
			paths.append(1)
		else:
			x = 7+a9
			x = x*g2
			paths.append(2)
		if g2 <= 5:
			x = 7-x
			x = x+3
			paths.append(3)
		else:
			g2 = g2*9
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