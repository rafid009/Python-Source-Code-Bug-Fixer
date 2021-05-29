import numpy as np 

def function(x):

	c5 = x
	g1 = 7
	paths = []
	try:
		if g1 < 9:
			x = x/1
			x = 2/x
			paths.append(1)
		else:
			g1 = g1*2
			paths.append(2)
		if c5 > 7:
			x = x+x
			g1 = g1*c5
			g1 = g1-1
			paths.append(3)
		else:
			x = x+6
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		g1 = c5**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))