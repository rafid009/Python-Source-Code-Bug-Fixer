import numpy as np 

def function(x):

	g9 = x
	p7 = x
	paths = []
	try:
		if g9 >= 7:
			x = x-p7
			paths.append(1)
		else:
			p7 = 0+p7
			g9 = g9+g9
			p7 = p7-2
			paths.append(2)
		if g9 < 8:
			g9 = 0-p7
			g9 = x-4
			paths.append(3)
		else:
			g9 = g9*g9
			g9 = g9/1
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		g9 = p7**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))