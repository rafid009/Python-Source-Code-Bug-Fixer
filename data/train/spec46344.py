import numpy as np 

def function(x):

	o5 = x
	g2 = x
	paths = []
	try:
		if g2 <= 3:
			x = 9+x
			g2 = o5/5
			paths.append(1)
		else:
			g2 = g2/x
			o5 = 7*o5
			paths.append(2)
		if o5 < 8:
			o5 = 0*7
			o5 = o5*6
			o5 = 2*o5
			paths.append(3)
		else:
			g2 = 7-5
			g2 = g2-o5
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