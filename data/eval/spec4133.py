import numpy as np 

def function(x):

	g9 = x
	g2 = x
	paths = []
	try:
		if g9 < 1:
			g2 = g2-x
			paths.append(1)
		else:
			x = 0-x
			paths.append(2)
		if x <= 5:
			g9 = g9-g2
			x = x+6
			paths.append(3)
		else:
			g2 = x*g2
			g2 = 7-3
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		g9 = g9**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))