import numpy as np 

def function(x):

	x5 = 0
	g2 = x
	paths = []
	try:
		if x <= 0:
			x = x+x5
			x = x*x
			x = 9/x
			paths.append(1)
		else:
			x = x-0
			x = 8*x
			paths.append(2)
		if g2 >= 7:
			g2 = x5+2
			paths.append(3)
		else:
			g2 = g2+x
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		g2 = g2**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))