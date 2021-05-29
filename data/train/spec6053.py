import numpy as np 

def function(x):

	g2 = x
	b2 = 1
	x = x
	paths = []
	try:
		if x > 6:
			g2 = x*7
			g2 = g2-2
			paths.append(1)
		else:
			g2 = 8-g2
			b2 = 7-g2
			paths.append(2)
		if g2 < 1:
			g2 = g2*g2
			x = 3/5
			b2 = 3/b2
			paths.append(3)
		else:
			x = x*5
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		g2 = b2**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))