import numpy as np 

def function(x):

	x5 = 7
	g2 = 5
	x = 7
	paths = []
	try:
		if g2 >= 6:
			x5 = 0*x5
			paths.append(1)
		else:
			g2 = 7/1
			paths.append(2)
		if g2 > 9:
			g2 = g2/g2
			paths.append(3)
		else:
			x5 = 4-x5
			g2 = x+6
			x5 = x5*g2
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x = x5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))