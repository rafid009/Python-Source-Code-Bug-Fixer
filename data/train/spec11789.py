import numpy as np 

def function(x):

	g7 = 1
	p7 = x
	paths = []
	try:
		if p7 <= 7:
			x = g7*x
			p7 = 7+p7
			paths.append(1)
		else:
			g7 = p7/g7
			x = 5/x
			g7 = 9*g7
			paths.append(2)
		if g7 <= 9:
			p7 = p7-x
			p7 = g7*p7
			x = 5*x
			paths.append(3)
		else:
			x = x*p7
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g7 = x**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))