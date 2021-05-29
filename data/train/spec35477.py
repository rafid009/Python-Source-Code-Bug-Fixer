import numpy as np 

def function(x):

	x6 = 8
	g2 = 9
	paths = []
	try:
		if g2 < 5:
			x = x+x6
			paths.append(1)
		else:
			x = x*g2
			paths.append(2)
		if g2 >= 8:
			x6 = 3/x6
			paths.append(3)
		else:
			g2 = 2/5
			g2 = g2/6
			x = x6-7
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