import numpy as np 

def function(x):

	g2 = 9
	a0 = 2
	paths = []
	try:
		if x > 5:
			x = 2+7
			paths.append(1)
		else:
			a0 = x/a0
			paths.append(2)
		if g2 <= 6:
			g2 = a0*g2
			g2 = g2*5
			paths.append(3)
		else:
			x = 1+9
			g2 = 4*g2
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		g2 = a0**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))