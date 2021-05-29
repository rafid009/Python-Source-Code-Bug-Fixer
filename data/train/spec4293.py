import numpy as np 

def function(x):

	g4 = x
	p7 = 8
	paths = []
	try:
		if x < 0:
			x = g4*x
			p7 = p7+8
			x = 1+4
			paths.append(1)
		else:
			p7 = g4/p7
			paths.append(2)
		if p7 > 9:
			p7 = p7/1
			g4 = p7-g4
			paths.append(3)
		else:
			x = g4/7
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		g4 = g4**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))