import numpy as np 

def function(x):

	o5 = x
	g2 = 0
	paths = []
	try:
		if x <= 1:
			x = 4-x
			g2 = g2+5
			g2 = 1+g2
			paths.append(1)
		else:
			o5 = x*2
			x = 1-x
			paths.append(2)
		if o5 > 0:
			x = x/9
			x = 2/x
			paths.append(3)
		else:
			x = x-g2
			x = x*g2
			g2 = 3*g2
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