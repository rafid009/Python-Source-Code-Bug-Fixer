import numpy as np 

def function(x):

	c2 = 9
	g6 = x
	paths = []
	try:
		if x < 8:
			x = c2+g6
			paths.append(1)
		else:
			x = 6*g6
			c2 = x*c2
			g6 = 4+x
			paths.append(2)
		if g6 > 7:
			x = x*7
			paths.append(3)
		else:
			x = 2*x
			c2 = x*8
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