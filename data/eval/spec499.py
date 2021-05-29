import numpy as np 

def function(x):

	r1 = x
	g2 = x
	paths = []
	try:
		if g2 >= 2:
			r1 = 1/r1
			r1 = 7+4
			g2 = g2/x
			paths.append(1)
		else:
			x = x*9
			paths.append(2)
		if x < 3:
			g2 = g2-9
			g2 = 1/r1
			g2 = 0/3
			paths.append(3)
		else:
			r1 = 5-5
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