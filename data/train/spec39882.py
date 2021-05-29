import numpy as np 

def function(x):

	g5 = 4
	c8 = x
	x = 2
	paths = []
	try:
		if g5 < 8:
			g5 = 7*6
			g5 = g5-x
			g5 = 2-8
			paths.append(1)
		else:
			g5 = 2+g5
			paths.append(2)
		if c8 > 7:
			x = 3*x
			g5 = g5/c8
			c8 = 0+9
			paths.append(3)
		else:
			c8 = 6*0
			x = x/g5
			g5 = g5+8
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		g5 = g5**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))