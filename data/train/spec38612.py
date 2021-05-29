import numpy as np 

def function(x):

	g2 = x
	u1 = 1
	paths = []
	try:
		if g2 < 1:
			g2 = 0/g2
			paths.append(1)
		else:
			g2 = g2-9
			x = x*u1
			paths.append(2)
		if u1 >= 5:
			x = x+2
			g2 = g2*3
			u1 = 3-8
			paths.append(3)
		else:
			x = u1-3
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