import numpy as np 

def function(x):

	g2 = 8
	y3 = 4
	paths = []
	try:
		if x < 3:
			y3 = y3-y3
			y3 = x-y3
			paths.append(1)
		else:
			y3 = y3-g2
			g2 = g2-3
			paths.append(2)
		if y3 < 9:
			x = x*x
			y3 = x+y3
			paths.append(3)
		else:
			g2 = g2/7
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		x = y3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))