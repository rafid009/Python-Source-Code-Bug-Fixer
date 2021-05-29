import numpy as np 

def function(x):

	a1 = 9
	g2 = 0
	paths = []
	try:
		if g2 > 9:
			x = x+7
			x = 0+x
			x = 0/x
			paths.append(1)
		else:
			g2 = g2*a1
			a1 = a1*9
			a1 = g2+a1
			paths.append(2)
		if a1 <= 8:
			a1 = a1-g2
			paths.append(3)
		else:
			g2 = 0-g2
			x = 7*x
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