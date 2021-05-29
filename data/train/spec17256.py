import numpy as np 

def function(x):

	g2 = x
	c2 = x
	paths = []
	try:
		if x < 8:
			g2 = 8/x
			c2 = c2+6
			c2 = c2-1
			paths.append(1)
		else:
			c2 = 1*x
			paths.append(2)
		if g2 > 3:
			x = 8*x
			c2 = c2/9
			c2 = c2/1
			paths.append(3)
		else:
			c2 = c2+6
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		x = g2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))