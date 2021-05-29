import numpy as np 

def function(x):

	g2 = x
	g0 = 1
	paths = []
	try:
		if x <= 5:
			g2 = g2*g2
			paths.append(1)
		else:
			g0 = g0/4
			g2 = x*g2
			g0 = g0-5
			paths.append(2)
		if x < 6:
			x = 9+x
			g2 = g2-3
			g2 = g2/8
			paths.append(3)
		else:
			g0 = g0+g2
			g2 = g2-5
			g0 = g0*x
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		x = g0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))