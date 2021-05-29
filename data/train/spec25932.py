import numpy as np 

def function(x):

	q8 = x
	g2 = 1
	paths = []
	try:
		if q8 > 6:
			q8 = q8+x
			q8 = q8-5
			paths.append(1)
		else:
			g2 = g2-x
			g2 = g2/1
			paths.append(2)
		if q8 <= 6:
			g2 = q8-g2
			paths.append(3)
		else:
			x = g2*g2
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