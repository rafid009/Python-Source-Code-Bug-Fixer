import numpy as np 

def function(x):

	c1 = x
	g8 = x
	paths = []
	try:
		if c1 > 5:
			c1 = 7/c1
			c1 = c1+5
			x = x*6
			paths.append(1)
		else:
			g8 = g8*7
			paths.append(2)
		if g8 <= 7:
			g8 = x+0
			paths.append(3)
		else:
			g8 = g8+x
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		x = c1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))