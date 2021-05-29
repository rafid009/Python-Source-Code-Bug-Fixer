import numpy as np 

def function(x):

	u6 = 5
	g2 = 3
	paths = []
	try:
		if g2 >= 3:
			x = g2-x
			g2 = g2-6
			paths.append(1)
		else:
			g2 = 5/g2
			paths.append(2)
		if x >= 7:
			u6 = 0-3
			g2 = g2-6
			paths.append(3)
		else:
			g2 = 0-0
			g2 = g2/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u6 = x**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))