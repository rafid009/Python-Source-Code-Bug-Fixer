import numpy as np 

def function(x):

	g2 = 4
	a9 = 5
	paths = []
	try:
		if x >= 8:
			g2 = g2+9
			g2 = g2*7
			x = x*x
			paths.append(1)
		else:
			g2 = x-g2
			g2 = 7*g2
			g2 = g2/x
			paths.append(2)
		if g2 < 8:
			g2 = g2+3
			a9 = 9-2
			g2 = 7+g2
			paths.append(3)
		else:
			x = x-5
			a9 = a9-1
			g2 = g2*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a9 = x**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))