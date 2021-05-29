import numpy as np 

def function(x):

	g2 = 3
	x4 = x
	paths = []
	try:
		if x4 <= 1:
			g2 = 5*x
			paths.append(1)
		else:
			x = 6*4
			x = 1-6
			g2 = 3*4
			paths.append(2)
		if x4 < 9:
			x4 = x4*8
			x = x+2
			paths.append(3)
		else:
			g2 = g2-4
			x = x+x4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))