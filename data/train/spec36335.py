import numpy as np 

def function(x):

	k7 = 9
	g2 = 3
	x = x
	paths = []
	try:
		if x <= 7:
			k7 = k7/7
			k7 = 8+k7
			g2 = g2/g2
			paths.append(1)
		else:
			x = x/5
			paths.append(2)
		if x >= 3:
			g2 = 3+k7
			x = k7+x
			paths.append(3)
		else:
			g2 = g2-x
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