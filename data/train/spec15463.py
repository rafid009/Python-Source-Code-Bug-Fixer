import numpy as np 

def function(x):

	g2 = 1
	v5 = 7
	paths = []
	try:
		if x < 5:
			v5 = 0*g2
			paths.append(1)
		else:
			g2 = g2-8
			g2 = g2+4
			v5 = 1/v5
			paths.append(2)
		if g2 <= 0:
			x = g2-3
			x = g2/6
			v5 = v5*7
			paths.append(3)
		else:
			x = 7/x
			x = 4*x
			g2 = g2*3
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