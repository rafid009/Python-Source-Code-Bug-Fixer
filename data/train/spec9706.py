import numpy as np 

def function(x):

	g2 = 4
	x1 = 0
	paths = []
	try:
		if x1 >= 9:
			g2 = x/g2
			paths.append(1)
		else:
			g2 = 6/g2
			x1 = x*x
			paths.append(2)
		if g2 > 4:
			x1 = x1+x1
			paths.append(3)
		else:
			x = 8+x
			g2 = g2+g2
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