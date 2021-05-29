import numpy as np 

def function(x):

	g2 = x
	n2 = 3
	paths = []
	try:
		if n2 < 4:
			n2 = n2+4
			n2 = 6*g2
			n2 = 5*x
			paths.append(1)
		else:
			n2 = n2*5
			paths.append(2)
		if x >= 0:
			n2 = n2*3
			paths.append(3)
		else:
			g2 = 4-8
			n2 = n2/8
			g2 = x+g2
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