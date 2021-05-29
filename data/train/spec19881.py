import numpy as np 

def function(x):

	g0 = 6
	p7 = x
	paths = []
	try:
		if p7 <= 1:
			g0 = g0*x
			paths.append(1)
		else:
			p7 = 2-p7
			g0 = g0*9
			paths.append(2)
		if p7 >= 7:
			p7 = x*p7
			g0 = g0-3
			p7 = 3+3
			paths.append(3)
		else:
			g0 = 1-g0
			x = x*p7
			p7 = g0*p7
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		g0 = p7**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))