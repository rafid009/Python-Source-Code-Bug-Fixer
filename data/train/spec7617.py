import numpy as np 

def function(x):

	g2 = 6
	h9 = 4
	paths = []
	try:
		if g2 <= 3:
			g2 = g2+0
			paths.append(1)
		else:
			g2 = h9*h9
			paths.append(2)
		if x < 3:
			g2 = h9*7
			h9 = x-1
			x = x+x
			paths.append(3)
		else:
			h9 = 9/4
			x = x/x
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		g2 = h9**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))